# -*- coding: utf-8 -*-
#

import xbmcaddon
from utilities import Debug, checkSettings, getTraktSettings
from notification_service import NotificationService

__addon__ = xbmcaddon.Addon("script.trakt")
__addonversion__ = __addon__.getAddonInfo('version')
__addonid__ = __addon__.getAddonInfo('id')
__language__ = __addon__.getLocalizedString

Debug("Loading '%s' version '%s'" % (__addonid__, __addonversion__))

# starts update/sync
def autostart():
	if checkSettings(True):
		getTraktSettings()
		# startup notifcation service
		NotificationService()
	
	Debug("Plugin shutting down.")

autostart()
