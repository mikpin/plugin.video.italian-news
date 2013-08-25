import sys, xbmcplugin, xbmcgui

_id = "plugin.video.italian-news"
_resdir = "special://home/addons" + _id + "/resources"
_thisPlugin = int(sys.argv[1])

sys.path.append( _resdir + "/lib/")

def _addItem(label,uri):
    item = xbmcgui.ListItem(label)
    xbmcplugin.addDirectoryItem(_thisPlugin,uri,item)

def _get_params():
    param=[] _addItem('paolo','') _addItem('luca','')
    paramstring=sys.argv[2] xbmcplugin.endOfDirectory(_thisPlugin)
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
