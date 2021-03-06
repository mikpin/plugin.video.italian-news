import sys, xbmcplugin, xbmcgui,xbmc

_id = "plugin.video.italian-news"
_resdir = "special://home/addons/" + _id + "/resources"
_thisPlugin = int(sys.argv[1])
_icons = _resdir + "/icons/"

sys.path.append( xbmc.translatePath(_resdir + "/lib/"))
import rai

_tg1Icon=xbmc.translatePath(_icons +"Tg1_logo.png")
_tg2Icon=xbmc.translatePath(_icons +"Tg2_logo.png")
_tg3Icon=xbmc.translatePath(_icons +"Tg3_logo.png")

def _addItem(label,uri,icon,isFolder=False):
    item = xbmcgui.ListItem(label, iconImage=icon)
    xbmcplugin.addDirectoryItem(_thisPlugin,uri,item,isFolder)

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

param = _get_params()
plugins = {
    '1':(rai.RaiUno, 'Guarda il TG1',_tg1Icon),
    '2':(rai.RaiDue, 'Guarda il TG2',_tg2Icon),
    '3':(rai.RaiTre, 'Guarda il TG3',_tg3Icon)
    }

if 'plugin' in param:
    (engine, title, eicon)=plugins[param['plugin']]
    for (name,url,icon) in engine().get():
        if icon == '':
            icon = eicon
        _addItem(name,url,icon)
    xbmcplugin.endOfDirectory(_thisPlugin)
else:
    for n in sorted(plugins.iterkeys()):
        (engine, title, icon)=plugins[n]
        print title
        _addItem(title,sys.argv[0]+'?plugin='+n,icon,isFolder=True)
    xbmcplugin.endOfDirectory(_thisPlugin)
    
#for (name,url,icon) in tg1:
#    _addItem(name,url,icon)
#xbmcplugin.endOfDirectory(_thisPlugin)
