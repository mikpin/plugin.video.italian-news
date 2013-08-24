import sys, xbmcplugin, xbmcgui

_id = "plugin.video.italian-news"
_resdir = "special://home/addons" + _id + "/resources"
_thisPlugin = int(sys.argv[1])

sys.path.append( _resdir + "/lib/")

def _addItem(label,uri):
    item = xbmcgui.ListItem(label)
    xbmcplugin.addDirectoryItem(_thisPlugin,uri,item)

_addItem('paolo','')
_addItem('luca','')

xbmcplugin.endOfDirectory(_thisPlugin)
