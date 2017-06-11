import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Project X Wizard'
EXCLUDES       = [ADDON_ID, 'tvsupertuga.repository']
EXCLUDES       = [ADDON_ID, 'projectx.wizard']
# Text File with build info in it.
BUILDFILE      = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/wizard.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Project X Youtube'
YOUTUBEFILE    = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/advancedsettings.txt'
# Text file for roms and emus
ROMPACK        = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/rom-packs.txt.txt'
EMUAPKS        = 'https://xprojectx.000webhostapp.com/projectxwizard2/sub/emuapks.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONMAINT      = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONSPEED      = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONAPK        = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONRETRO      = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONADDONS     = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONYOUTUBE    = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONSAVE       = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONTRAKT      = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONREAL       = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONLOGIN      = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONCONTACT    = 'https://i58.servimg.com/u/f58/19/44/91/43/fanart17.jpg'
ICONSETTINGS   = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
ICONWIZARD1URL   = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
#COLOR1         = 'dodgerblue'
#COLOR2         = 'yellow'
COLOR1         = 'snow'
COLOR2         = 'floralwhite'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+''+COLOR2+''+COLOR2+']%s[/COLOR]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Project X Wizard                    tvsupertuga@gmail.com'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
CONTACTFANART  = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'https://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'tvsupertuga.repository'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://ftgyhujiko.000webhostapp.com/tvsupertuga.repository/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://ftgyhujiko.000webhostapp.com/tvsupertuga.repository/instal/tvsupertuga.repository/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://xprojectx.000webhostapp.com/projectxwizard2/projectxwizard.xml'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'Project X Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'https://i58.servimg.com/u/f58/19/44/91/43/projec10.png'
#########################################################