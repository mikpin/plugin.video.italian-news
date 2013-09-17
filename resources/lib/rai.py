import urllib2, json
from operator import itemgetter

"""
class RaiNews:
    def __init__(self):
        pass
    def load(self,uri):
        f = urllib2.urlopen(uri)
        data = f.read()
        return (f.getcode() , data)
    def parseItemXML(self,itemXMLurl):
        (code,itemXML) = self.load(itemXMLurl)
        try:
            xml = ElementTree.fromstring(itemXML)
        except:
            pass
        item = xml.find('./item')
        name = item.attrib['name']
        videoUnitURL = xml.find('./item/units/videoUnit/url').text
        try:
            imageUnitURL = self.baseUrl+xml.find('./item/units/imageUnit/image').text
        except:
            imageUnitURL = ''
        videoUnitAttribute =xml.find('./item/units/videoUnit/attributes').findall('./attribute')
        
        for node in videoUnitAttribute:
            key = node.find('key').text
            value = node.find('value').text
            if (key=='h264'):
                videoUnitURL = value
        
        return (name,videoUnitURL, imageUnitURL)

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
                

class RaiDue(RaiNews):
    def __init__(self):
        self.baseUrl="http://www.tg2.rai.it/"
        self.reEdizione = re.compile('<a data-ediz="(.*?)"(.*?)data-uniq="(.*?)"',re.DOTALL)
    def get(self):
        ret = []
        (code,html) = self.load(self.baseUrl)
        edizioni = self.reEdizione.finditer(html)
        for e in edizioni:
            itemXMLurl = self.baseUrl+'/dl/RaiTV/programmi/media/'+e.group(3)+'.xml'
            ret.append( self.parseItemXML(itemXMLurl))
        return ret
"""
class RaiJson():
    def __init__(self):
        self.content = []
        pass
    def load(self,uri):
        print "loading: " + uri
        f = urllib2.urlopen(uri)
        data = f.read()
        return (f.getcode() , data)
    def loadPage(self,page):
        return self.load('http://www.rai.tv/dl/RaiTV/programmi/json/liste/' + self.content + '-json-V-'+str(page)+'.html')
    def loadContent(self):
        ret = []
        for c in self.content:
            (error,jsonRai) =self.load('http://www.rai.tv/dl/RaiTV/programmi/json/liste/' + c + '-json-V-0.html')
            data= json.loads(jsonRai)
            list = data['list']
            ret = ret+list
        ret=sorted(ret, key=itemgetter('name'))
        return ret
    def get(self,page = 0):
        list = self.loadContent()
        ret=[]
        for e in list:
            image = ''
            if e['image_433'] != '':
                image = 'http://www.rai.tv'+e['image_433']
            ret.append((e['name'],e['h264'],image))
        return ret

class RaiUno(RaiJson):
    def __init__(self):
        self.content = ['ContentSet-fb594231-cfb2-4e5a-b121-196ca772e335']

class RaiDue(RaiJson):
    def __init__(self):
        self.content = ['ContentSet-995870b7-67cf-4e13-ab9c-2cbabd026d7e','ContentSet-46ce6c60-c7f2-446c-8a61-fc2153fbe2d3',
            'ContentSet-5e2e70b2-f815-46ee-9011-d5fce1569147','ContentSet-81bb6f30-9284-439a-aaa4-21a5c91652b7']
            
class RaiTre(RaiJson):
    def __init__(self):
        self.content = ["ContentSet-386b19cb-40f7-447c-8cb5-eb32ece56701","ContentSet-6734e497-4206-4669-88c5-91a7a5f00a9b","ContentSet-9e4448b6-0998-4d63-937d-27b1651c6f86"]
            
if __name__ =='__main__':
    rai1 = RaiUno()
    print rai1.get()
