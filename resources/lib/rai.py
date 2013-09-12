import urllib2,re
import xml.etree.ElementTree as ElementTree

class RaiNews:
    def __init__(self):
        pass
    def load(self,uri):
        f = urllib2.urlopen(uri)
        data = f.read()
        return (f.getcode() , data)

class RaiUno(RaiNews):
    def __init__(self):
        self.baseUrl="http://www.tg1.rai.it/"
        self.reEdizione = re.compile("<li class=\"Edizione\" id=\"(.*?)\">.*?<span>(.*?)</span>(.*?)</a>.</li>",re.DOTALL)
        self.reItem = re.compile("initEdizione..(.*?)'")
    def get (self, xuri=0):
        if (xuri ==0):
            (code,html) = self.load(self.baseUrl)
            edizioni = self.reEdizione.finditer(html)
            ret = []
            for e in edizioni:
                popUrl=self.baseUrl+'/dl/tg1/2010/edizioni/'+e.group(1)+'-tg1.html'
                (code,popHtml)=self.load(popUrl)
                itemId =  self.reItem.search(popHtml).group(1)
                itemXMLurl = self.baseUrl+'/dl/RaiTV/programmi/media/'+itemId+'.xml'
                (code,itemXML) = self.load(itemXMLurl)
                try:
                    xml = ElementTree.fromstring(itemXML)
                except:
                    pass
                item = xml.find('./item')
                name = item.attrib['name']
                videoUnitURL = xml.find('./item/units/videoUnit/url').text
                imageUnitURL = self.baseUrl+xml.find('./item/units/imageUnit/image').text
                videoUnitAttribute =xml.find('./item/units/videoUnit/attributes').findall('./attribute')
                for node in videoUnitAttribute:
                    key = node.find('key').text
                    value = node.find('value').text
                    if (key=='h264'):
                        videoUnitURL = value
                ret.append( (name,videoUnitURL, imageUnitURL))
            return ret
                

if __name__ =='__main__':
    rai1 = RaiUno()
    print rai1.get()
