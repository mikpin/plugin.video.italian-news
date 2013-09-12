import sys, xbmcplugin, xbmcgui,xbmc

_id = "plugin.video.italian-news"
_resdir = "special://home/addons/" + _id + "/resources"
_thisPlugin = int(sys.argv[1])
_icons = _resdir + "/icons/"

sys.path.append( xbmc.translatePath(_resdir + "/lib/"))
import rai

_tg1Icon=xbmc.translatePath(_icons +"tg1.jpg")


def _addItem(label,uri,icon):
    item = xbmcgui.ListItem(label, iconImage=icon)
    xbmcplugin.addDirectoryItem(_thisPlugin,uri,item)

def _get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                    params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                    splitparams={}
                    splitparams=pairsofparams[i].split('=')
                    if (len(splitparams))==2:
                            param[splitparams[0]]=splitparams[1]
    return param

tg1 = rai.RaiUno().get()
print param
for (name,url,icon) in tg1:
    _addItem(name,url,icon)
xbmcplugin.endOfDirectory(_thisPlugin)
