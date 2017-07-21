import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,shutil,urlresolver,random,liveresolver,hashlib,time
from resources.libs.common_addon import Addon
from resources.libs.modules import regex
import base64
from metahandler import metahandlers

addon_id        = 'plugin.audio.podbay'
addon           = Addon(addon_id, sys.argv)
selfAddon       = xbmcaddon.Addon(id=addon_id)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
searchicon      = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'search.jpg'))
nextpage        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'next.jpg'))
sd_path         = xbmc.translatePath(os.path.join('special://home/addons/', 'plugin.video.sportsdevil'))
baseurl         = 'https://pastebin.com/raw/k4BY3kDF'
ytpl            = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
ytpl2           = '&maxResults=50&key=AIzaSyAd-YEOqZz9nXVzGtn3KWzYLbLaajhqIDA'
ytplpg1         = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
ytplpg2         = '&part=snippet&playlistId='
ytplpg3         = '&maxResults=50&key=AIzaSyAvB3XWYEqUQPFoVMWssjqJhyeJOMi3A8g'
adultpass       = selfAddon.getSetting('password')
metaset         = selfAddon.getSetting('enable_meta')
messagetext     = 'https://pastebin.com/raw/JrCSGApd'
livematches     = ''
RUNNER 			= base64.b64decode(b'aHR0cDovL3NpbXRlY2gubmV0MTYubmV0L3lvdXR1YmUucGhwP2lkPQ==')
dialog = xbmcgui.Dialog()

def GetMenu():
        popup()
        xbmc.executebuiltin('Container.SetViewMode(500)')
        url = baseurl
        link=open_url(baseurl)
        match= re.compile('<item>(.+?)</item>').findall(link)
        for item in match:
            try:
                if '<m3u>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<m3u>(.+?)</m3u>').findall(item)[0]
                        addDir(name,url,11,iconimage,fanart)
                elif '<mamahdsports>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<mamahdsports>(.+?)</mamahdsports>').findall(item)[0]
                        addDir(name,url,14,iconimage,fanart)
                elif '<bigsports>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<bigsports>(.+?)</bigsports>').findall(item)[0]
                        addDir(name,url,13,iconimage,fanart)
                elif '<mamahd>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<mamahd>(.+?)</mamahd>').findall(item)[0]
                        addDir(name,url,12,iconimage,fanart)
                elif '<channel>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                        addDir(name,url,6,iconimage,fanart)
                elif '<podcasts>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<podcasts>(.+?)</podcasts>').findall(item)[0]
                        addDir(name,url,35,iconimage,fanart)
                elif '<sportsdevil>' in item:
                        links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                        if len(links)==1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                             url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                             referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                             check = referer
                             suffix = "/"
                             if not check.endswith(suffix):
                                 refer = check + "/"
                             else:
                                 refer = check
                             link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                             url = link + '%26referer=' +refer
                             addItem(name,url,4,iconimage,fanart)   
                        elif len(links)>1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                             fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                             addItem(name,url2,8,iconimage,fanart)       
                elif '<folder>'in item:
                                data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                for name,url,iconimage,fanart in data:
                                        addDir(name,url,1,iconimage,fanart)
                else:
                                links=re.compile('<link>(.+?)</link>').findall(item)
                                if len(links)==1:
                                        data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                        lcount=len(match)
                                        for name,url,iconimage,fanart in data:
                                                if 'youtube.com/playlist' in url:
                                                        addDir(name,url,2,iconimage,fanart)
                                                else:
                                                        addLink(name,url,2,iconimage,fanart)
                                elif len(links)>1:
                                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                                        addLink(name,url2,3,iconimage,fanart)
            except:pass
#            view(link)
#        icon = 'http://i.imgur.com/iTynJGx.jpg'
#        addItem('[B][COLOR aqua]'+'Real Debrid Login'+'[/COLOR]''[/B]','url',17,icon,fanarts)
def popup():
        message=open_url2(messagetext)
        if len(message)>1:
                path = xbmcaddon.Addon().getAddonInfo('path')
                comparefile = os.path.join(os.path.join(path,''), 'compare.txt')
                r = open(comparefile)
                compfile = r.read()       
                if compfile == message:pass
                else:
                        showText('[COLOR skyblue][B]PODBAY INFO[/COLOR][/B]', message)
                        text_file = open(comparefile, "w")
                        text_file.write(message)
                        text_file.close()
                        
def resolver_settings():
    urlresolver.display_settings()
                        
def GetContent(name,url,iconimage,fanart):

        if url == "":
            message=open_url2("")
            showText('[B][COLOR gold]Live Matches[/COLOR][/B]', message)
        hash = []
        url2=url
        link=open_url(url)
        if 'XXX>yes</XXX' in link:
		if adultpass == '':
		    dialog = xbmcgui.Dialog()
		    ret = dialog.yesno('Adult Content', 'You have opted to show adult content','','Please set a password to prevent accidental access','Cancel','OK')
		    if ret == 1:
			keyb = xbmc.Keyboard('', 'Set Password')
			keyb.doModal()
			if (keyb.isConfirmed()):
			    passw = keyb.getText()
			    selfAddon.setSetting('password',passw)
                    else:quit()
				    
	if 'XXX>yes</XXX' in link:
		if adultpass <> '':
			dialog = xbmcgui.Dialog()
			ret = dialog.yesno('Adult Content', 'Please enter the password you set','to continue','','Cancel','OK')
			if ret == 1:    
				keyb = xbmc.Keyboard('', 'Enter Password')
				keyb.doModal()
				if (keyb.isConfirmed()):
					passw = keyb.getText()
				if passw <> adultpass:
					quit()
			else:quit()
        match= re.compile('<item>(.+?)</item>').findall(link)
        for item in match:
            try:

                if '<regex>' in item:
                    regdata = re.compile('(<regex>.+?</regex>)', re.MULTILINE|re.DOTALL).findall(item)
                    regdata = ''.join(regdata)
                    reglist = re.compile('(<listrepeat>.+?</listrepeat>)', re.MULTILINE|re.DOTALL).findall(regdata)
                    regdata = urllib.quote_plus(regdata)

                    reghash = hashlib.md5()
                    for i in regdata: reghash.update(str(i))
                    reghash = str(reghash.hexdigest())

                    item = item.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
                    item = re.sub('<regex>.+?</regex>','', item)
                    item = re.sub('<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>','', item)
                    item = re.sub('<link></link>','', item)

                    name = re.sub('<meta>.+?</meta>','', item)
                    try: name = re.findall('<title>(.+?)</title>', name)[0]
                    except: name = re.findall('<name>(.+?)</name>', name)[0]

                    try: date = re.findall('<date>(.+?)</date>', item)[0]
                    except: date = ''
                    if re.search(r'\d+', date): name += ' [COLOR red] Updated %s[/COLOR]' % date

                    try: image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
                    except: image2 = icon

                    try: fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
                    except: fanart2 = fanarts

                    try: meta = re.findall('<meta>(.+?)</meta>', item)[0]
                    except: meta = '0'

                    try: url = re.findall('<link>(.+?)</link>', item)[0]
                    except: url = '0'
                    url = url.replace('>search<', '><preset>search</preset>%s<' % meta)
                    url = '<preset>search</preset>%s' % meta if url == 'search' else url
                    url = url.replace('>searchsd<', '><preset>searchsd</preset>%s<' % meta)
                    url = '<preset>searchsd</preset>%s' % meta if url == 'searchsd' else url
                    url = re.sub('<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>','', url)

                    if not regdata == '':
                        hash.append({'regex': reghash, 'response': regdata})
                        url += '|regex=%s' % regdata

                    addLinkRegex(name,url,10,image2,fanart2,"")

                elif '<mamahdsports>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<mamahdsports>(.+?)</mamahdsports>').findall(item)[0]
                        addDir(name,url,14,iconimage,fanart)
                elif '<bigsports>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<bigsports>(.+?)</bigsports>').findall(item)[0]
                        addDir(name,url,13,iconimage,fanart)
                elif '<fullhigh>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<fullhigh>(.+?)</fullhigh>').findall(item)[0]
                        addDir(name,url,15,iconimage,fanart)
                elif '<mamahd>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<mamahd>(.+?)</mamahd>').findall(item)[0]
                        addDir(name,url,12,iconimage,fanart)
                elif '<m3u>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<m3u>(.+?)</m3u>').findall(item)[0]
                        addDir(name,url,11,iconimage,fanart)
                elif '<channel>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                        addDir(name,url,6,iconimage,fanart)
                elif '<image>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<image>(.+?)</image>').findall(item)[0]
                        addDir(name,iconimage,9,iconimage,fanart)
                elif '<indi>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<indi>(.+?)</indi>').findall(item)[0]
                        addDir(name,iconimage,18,iconimage,fanart)
                elif '<tvshed>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<tvshed>(.+?)</tvshed>').findall(item)[0]
                        addDir(name,iconimage,21,iconimage,fanart)
                elif '<tvsearch>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<tvsearch>(.+?)</tvsearch>').findall(item)[0]
                        addDir(name,iconimage,26,iconimage,fanart)
                elif '<tvtrend>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<tvtrend>(.+?)</tvtrend>').findall(item)[0]
                        addDir(name,iconimage,27,iconimage,fanart)
                elif '<mama>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<mama>(.+?)</mama>').findall(item)[0]
                        addDir(name,iconimage,28,iconimage,fanart)
                elif '<shighlights>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<shighlights>(.+?)</shighlights>').findall(item)[0]
                        addDir(name,url,29,iconimage,fanart)
                elif '<moviegenre>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<moviegenre>(.+?)</moviegenre>').findall(item)[0]
                        addDir(name,url,31,iconimage,fanart)
                elif '<sportsdevil>' in item:
                        links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                        if len(links)==1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                             url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                             referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                             check = referer
                             suffix = "/"
                             if not check.endswith(suffix):
                                 refer = check + "/"
                             else:
                                 refer = check
                             link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                             url = link + '%26referer=' +refer
                             addItem(name,url,4,iconimage,fanart)   
                        elif len(links)>1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                             fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                             addItem(name,url2,8,iconimage,fanart)
    
                elif '<folder>'in item:
                                data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                for name,url,iconimage,fanart in data:
                                        addDir(name,url,1,iconimage,fanart)
                else:
                                links=re.compile('<link>(.+?)</link>').findall(item)
                                if len(links)==1:
                                        data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                        lcount=len(match)
                                        for name,url,iconimage,fanart in data:
                                                if 'youtube.com/playlist' in url:
                                                        addDir(name,url,2,iconimage,fanart)
                                                else:
                                                        addLink(name,url,2,iconimage,fanart)
                                elif len(links)>1:
                                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                                        addLink(name,url2,3,iconimage,fanart)
            except:pass
        view(link)

def YOUTUBE_CHANNEL(url):

	CHANNEL = RUNNER + url
	link = open_url(CHANNEL)
	patron = "<video>(.*?)</video>"
	videos = re.findall(patron,link,re.DOTALL)

	items = []
	for video in videos:
		item = {}
		item["name"] = find_single_match(video,"<name>([^<]+)</name>")
		item["url"] = base64.b64decode(b"cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvcGxheS8/dmlkZW9faWQ9") + find_single_match(video,"<id>([^<]+)</id>")
		item["author"] = find_single_match(video,"<author>([^<]+)</author>")
		item["iconimage"] = find_single_match(video,"<iconimage>([^<]+)</iconimage>")
		item["date"] = find_single_match(video,"<date>([^<]+)</date>")
		
		addLink('[COLOR skyblue]' + item["name"] + ' - on ' + item["date"] + '[/COLOR]',item["url"],7,item["iconimage"],fanart)

def GET_REGEX(name,url,iconimage):

	r, x = re.findall('(.+?)\|regex=(.+?)$', url)[0]
	r += urllib.unquote_plus(x)
	url = regex.resolve(r)

	PLAYREGEX(name,url,iconimage)

def SEARCH():
	keyb = xbmc.Keyboard('', '[COLOR skyblue]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=searchterm.upper()
	else:quit()
	link=open_url(SEARCH_LIST)
	slist=re.compile('<link>(.+?)</link>').findall(link)
	for url in slist:
                url2=url
                link=open_url(url)
                entries= re.compile('<item>(.+?)</item>').findall(link)
                for item in entries:
                        match=re.compile('<title>(.+?)</title>').findall(item)
                        for title in match:
                                title=title.upper()
                                if searchterm in title:
                                    try:
                                        if '<sportsdevil>' in item:
                                                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                                                url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                                                referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                                                link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                                                url = link + '%26referer=' +referer
                                                if 'tp' in url:
                                                        addLink(name,url,4,iconimage,fanarts)       
                                        elif '<folder>'in item:
                                                        data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                                        for name,url,iconimage,fanart in data:
                                                                if 'tp' in url:
                                                                        addDir(name,url,1,iconimage,fanarts)
                                        else:
                                                        links=re.compile('<link>(.+?)</link>').findall(item)
                                                        if len(links)==1:
                                                                data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                                                lcount=len(match)
                                                                for name,url,iconimage,fanart in data:
                                                                        if 'youtube.com/playlist' in url:
                                                                                addDir(name,url,2,iconimage,fanarts)
                                                                        else:
                                                                                if 'tp' in url: 
                                                                                        addLink(name,url,2,iconimage,fanarts)
                                                        elif len(links)>1:
                                                                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                                                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                                                addLink(name,url2,3,iconimage,fanarts)
                                    except:pass       

def GET_M3U(name,url,iconimage):

        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        response=link
        response = response.replace('#AAASTREAM:','#A:')
        response = response.replace('#EXTINF:','#A:')
        matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)
        li = []
        for params, display_name, url in matches:
            item_data = {"params": params, "display_name": display_name, "url": url}
            li.append(item_data)
        list = []
        for channel in li:
            item_data = {"display_name": channel["display_name"], "url": channel["url"]}
            matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
            for field, value in matches:
                item_data[field.strip().lower().replace('-', '_')] = value.strip()
            list.append(item_data)
        for channel in list:
            name = GetEncodeString(channel["display_name"])
            url = GetEncodeString(channel["url"])
            url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
            addLinkRegex(name ,url, 2, icon, fanart,'')

def GETMULTI(name,url,iconimage):
	streamurl=[]
	streamname=[]
	streamicon=[]
	link=open_url(url)
	urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
	iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
	links=re.compile('<link>(.+?)</link>').findall(urls)
	i=1
	for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )
                i=i+1
	name='[COLOR skyblue]'+name+'[/COLOR]'
	dialog = xbmcgui.Dialog()
	select = dialog.select(name,streamname)
	if select < 0:
		quit()
	else:
		url = streamurl[select]
		print url
		if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
                elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
                else: stream_url=url
                liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
                liz.setPath(stream_url)
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                
def GETMULTI_SD(name,url,iconimage):

    
    sdbase = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
    streamurl=[]
    streamname=[]
    streamicon=[]
    streamnumber=[]
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(urls)
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    i=1

    for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                        streamnumber.append('Stream ' + str(i))
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )

                i=i+1
    name='[COLOR skyblue]'+name+'[/COLOR]'
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        check = streamname[select]
        suffix = "/"
        if not check.endswith(suffix):
              refer = check + "/"
        else:
              refer = check
        url = sdbase + streamurl[select] + "%26referer=" + refer
        print url

        xbmc.Player().play(url)

def SCRAPE_MAMAHD(url):

	try:
		link=open_url(url).replace('\n','').replace('\t','')
		name=url.split('/')[2]
		name=name.replace('.html','')
		allgames=re.compile('<div class="schedule">(.+?)<br><div id="pagination">').findall(link)[0]
		livegame=re.compile('<a href="(.+?)">.+?<img src="(.+?)"></div>.+?<div class="home cell">.+?<span>(.+?)</span>.+?<span>(.+?)</span>.+?</a>').findall(allgames)
		for url,iconimage,home,away in livegame:
			url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url + '%26referer=no'
			addLink(home + ' vs ' + away,url,2,iconimage,fanarts,'')
	except:
		dialog.ok("Podbay", "Sorry, we could not find any live links at the moment. Please try again later.")
		quit()
		
def SCRAPE_BIGSPORTS(url):

	try:
		link=open_url(url)
		name=url.split('/')[2]
		name=name.replace('.html','')
		livegame=re.compile("<td><strong>(.+?)</strong></td>.+?<a target=.+? href=(.+?) class=.+?",re.DOTALL).findall(link)
		for game,url in livegame:
			url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url + '%26referer=no'
			addLink(game,url,2,iconimage,fanarts,'')
	except:
		dialog.ok("Podbay", "Sorry, we could not find any live links at the moment. Please try again later.")
		quit()
		
def SCRAPE_MAMAHD_SPORTS_CHANNELS(url):

    try:
        link=open_url(url).replace('\n','').replace('\t','')
        name=url.split('/')[2]
        name=name.replace('.html','')
        allgames=re.compile('<div class="standard row channels">(.+?)<div class="standard row">').findall(link)[0]
        livegame=re.compile('<a href="(.+?)".+?<img src="(.+?)"><br><span>(.+?)</span></a>').findall(allgames)
        for url,iconimage,channel in livegame:
            url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url + '%26referer=no'
            addLink(channel,url,2,iconimage,fanarts,'')
    except:
        dialog.ok("Podbay", "And The Offside Flag Is Up No Link Available")
        quit()
        
def SCRAPE_FULLHIGH():

    url ='http://livefootballvideo.com/fullmatch'
    link=open_url(url).replace('\n','').replace('\t','')
    match = re.compile('<div class="cover">(.+?)</div>').findall(link)
    for links in match:
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        title = re.compile ('title="(.+?)"').findall(links)[0]
        icon = re.compile ('src="(.+?)"').findall(links)[0]
        if 'premier-league' in url:
            addDir(title,url,16,icon,fanarts,'')
            
    try:
        nextpage = re.compile ('rel="next" href="(.+?)">').findall(link)[0]
        icon = 'http://i.imgur.com/U4B3xFF.jpg'
        addDir("[COLOR red]" + "Next Page" + "[/COLOR]",nextpage,15,icon,fanarts,'')
    except:pass
    
def SCRAPE_FULLHIGH_GET(url,icon,fanart):

    addItem("[COLOR red]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]",'url',999,icon,fanart,'')
    link=open_url(url).replace('\n','').replace('\t','')
    match = re.compile ('<p style="text-align:center"><iframe(.+?)</p>').findall(link)
    
    for links in match:
        url = re.compile ('src="(.+?)"',re.DOTALL).findall(links)[0]
        url1 = str.lower(url)
        if '1e' in url1:
            title = '1st Half'
        else:
            title = '2nd Half'
        
        addItem(title,url,666,icon,fanart,'')
    
        

def PLAYSD(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(url, liz, False)

def PLAYREGEX(name,url,iconimage):

	name = name.replace('  ','')
	if not 'f4m'in url:
		if '.m3u8' in url:
			url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon
		elif '.ts'in url:
			url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon
	else: url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
	
	import urlresolver
	if urlresolver.HostedMediaFile(url).valid_url(): 
		stream_url = urlresolver.HostedMediaFile(url).resolve()
		liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
		liz.setPath(stream_url)
		xbmc.Player ().play(stream_url, liz, False)
		quit()
	else:
		stream_url=url
		liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
		liz.setPath(stream_url)
		xbmc.Player ().play(stream_url, liz, False)
		quit()

def PLAYLINK(name,url,iconimage):

        if not "http" in url:
            if '.ts'in url:
                url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon
            elif '.m3u8' in url:
                url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon
            elif '.mpegts'in url:
                url = url.replace('.mpegts','.m3u8')
                url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon

            liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
            xbmc.Player ().play(url, liz, False)
            quit()

        if not'http'in url:url='http://'+url
        if 'youtube.com/playlist' in url:
                searchterm = url.split('list=')[1]
                ytapi = ytpl + searchterm + ytpl2
                req = urllib2.Request(ytapi)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = link.replace('\r','').replace('\n','').replace('  ','')     
                match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
                try:
                        np=re.compile('"nextPageToken": "(.+?)"').findall(link)[0]
                        ytapi = ytplpg1 + np + ytplpg2 + searchterm + ytplpg3
                        addDir('Next Page >>',ytapi,2,nextpage,fanart)
                except:pass



                
                for name,ytid in match:
                        url = 'https://www.youtube.com/watch?v='+ytid
                        iconimage = 'https://i.ytimg.com/vi/'+ytid+'/hqdefault.jpg'
                        if not 'Private video' in name:
                                if not 'Deleted video' in name:
                                        addLink(name,url,2,iconimage,fanart)
                
        if 'https://www.googleapis.com/youtube/v3' in url:
                searchterm = re.compile('playlistId=(.+?)&maxResults').findall(url)[0]
                req = urllib2.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req)
                link=response.read()
                response.close()
                link = link.replace('\r','').replace('\n','').replace('  ','')     
                match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
                try:
                        np=re.compile('"nextPageToken": "(.+?)"').findall(link)[0]
                        ytapi = ytplpg1 + np + ytplpg2 + searchterm + ytplpg3
                        addDir('Next Page >>',ytapi,2,nextpage,fanart)
                except:pass


                
                for name,ytid in match:
                        url = 'https://www.youtube.com/watch?v='+ytid
                        iconimage = 'https://i.ytimg.com/vi/'+ytid+'/hqdefault.jpg'
                        if not 'Private video' in name:
                                if not 'Deleted video' in name:
                                        addLink(name,url,2,iconimage,fanart)



        if "plugin://" in url:
            url = "PlayMedia("+url+")"
            xbmc.executebuiltin(url)
            quit()

        if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
        elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
        else: stream_url=url
        liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                            
def PLAYVIDEO(url):

	xbmc.Player().play(url)
    
def SCRAPE_SPORTSHIGHLIGHTS_GAMES():

    url = 'http://www.goalsarena.org/en/'
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile ('<div class="videos"(.+?)<div class="moduletable-none">').findall(link)[0]
    grab = re.compile('<a title=".+?" href="(.+?)">(.+?)</a>').findall(match)
    
    for link1,game in grab:
        addDir("[COLOR aqua]" + game + "[/COLOR]",link1,30,icon,fanarts,'')
        
def SCRAPE_SPORTSHIGHLIGHTS_LINKS(url):

    
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    
    try:
        match = re.compile ('<div id="videodetailsarea"(.+?)</div>').findall(link)[0]
        match2 = re.compile ('<script data-config="(.+?)"').findall(match)[0]
        if not 'http' in match2:
            rl = 'http:' + (match2)
            link4 = open_url(rl)
            grab2= re.compile('"f4m":"(.+?)"').findall(link4)[0]
            link5 = open_url(grab2)
            playme = re.compile('<media url="(.+?)"').findall(link5)[2]
            liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
            xbmc.Player ().play(playme, liz, False)
    
        
    except: pass
    quit(0)
    
def SCRAPE_INDI():

    url = 'http://burningwhee1s.blogspot.co.uk/'
    link = open_url(url)
    match = re.compile('<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>').findall(link)[0]
    grab = re.compile ('<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>').findall(match)
    for link,title in grab:
        addDir("[COLOR aqua]" + title + "[/COLOR]",link,19,icon,fanarts,'')
        
def SCRAPE_INDI_CONTENT(url):

    link = open_url(url)
    match = re.compile('<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>').findall(link)
    for links in match:
        title = re.compile ('<a href=\'.+?\'>(.+?)</a>').findall(links)[0]
        icon = re.compile ('<img border=".+?" src="(.+?)"').findall(links)[0]
        url = re.compile ('<a href=\'(.+?)\'').findall(links)[0]
        addDir("[COLOR aqua]" + title + "[/COLOR]",url,20,icon,fanarts,'')
        
def SCRAPE_INDI_LINKS(url,iconimage):

    link = open_url(url)
    match = re.compile('<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>').findall(link)[0]
    grab = re.compile ('<div class=".+?" style=".+?">(.+?)</select>').findall(match)
    for links in grab:
        title = re.compile ('<b>(.+?)</b>').findall(links)[0].replace('<span style="font-size: large;">', '').replace('</span>', '')
        try:
            title2 = re.compile ('<b>(.+?)</b>').findall(links)[3].replace('<span style="font-size: large;">', '').replace('</span>', '')
        except IndexError:
            try:
                title2 = re.compile ('<b>(.+?)</b>').findall(links)[2].replace('<span style="font-size: large;">', '').replace('</span>', '')
            except IndexError:
                title2 = ''
        title = CLEANUP(title)
        title2 = CLEANUP(title2)
        video = re.compile ('<option value="(.+?)"').findall(links)[1]
        addLink("[COLOR aqua]" + title + "  " + title2 + "[/COLOR]",video,666,icon,fanarts,'')
        
def TV_SCHED():

    url = 'http://www.watchepisodeseries.com/home/schedule'
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="schedule-calendar">(.+?)</div>').findall(link)[0]
    grab = re.compile ('<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>').findall(match)
    for url,date,month in grab:
        addDir(date + "  " + month,url,22,icon,fanart)
  #  SET_VIEW()
    
def TV_SCHED_CONTENT(url,name,icon,fanart):

    addDir("[COLOR red]" + name + "[/COLOR]",'url',999,icon,fanart)
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="sl-box">(.+?)</div>').findall(link)
    for links in match:
        title = re.compile ('<a href=".+?">(.+?)</a>').findall(links)[1]
        title = CLEANUP(title)
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        icon = re.compile ('style="background-image:.+?\'(.+?)\'').findall(links)[0]
        fanart = re.compile ('style="background-image:.+?\'(.+?)\'').findall(links)[0]
        addDir(title,url,23,icon,fanart)
  #  SET_VIEW()
    
def TV_SCHED_CONTENT_GRAB(url,icon,fanart):

    
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="watched">(.+?)<div class="el-item">').findall(link)
    i = datetime.datetime.now()
    for links in match:
        try:
            url = re.compile ('<a href="(.+?)"').findall(links)[0]
            title = re.compile ('<div class="name">(.+?)</div>').findall(links)[0]
            title = CLEANUP(title)
            season = re.compile ('<div class="season">(.+?)</div>').findall(links)[0]
            epi = re.compile ('<div class="episode">(.+?)</div>').findall(links)[0]
            date = re.compile ('<div class="date">(.+?)</div>').findall(links)[0].replace('-', '/')
            if not 'Season 0' in season:
                if 'Air Date' not in date:
                    date = date.strip()
                    date = time.strptime(date, "%d/%m/%Y")
                    currentdate = ("%s/%s/%s" % (i.day, i.month, i.year) )
                    currentdate = time.strptime(currentdate, "%d/%m/%Y")
                    if (currentdate < date):
                        title = '[COLOR red]' + (title) + ' - Not Aired Yet' + '[/COLOR]'
                        epi = '[COLOR red]' + (epi) + '[/COLOR]'#
                        season = '[COLOR red]' + (season) + '[/COLOR]'
                    
                    addDir(season + " " + epi + " " + title,url,24,icon,fanart)
        except:pass
   # SET_VIEW() 
    
def TV_SCHED_CONTENT_GRAB_LINKS(url,icon,fanart):

    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="domain">(.+?)<div class="watch"').findall(link)
    for links in match:
        try:
            title = re.compile ('<a href=".+?">(.+?)</a>').findall(links)[0]
            title = title.title()
            title = CLEANUP(title)
            url = re.compile ('<a href="(.+?)"').findall(links)[0]
            addLink(title,url,25,iconimage,fanart)
        except:pass
   # SET_VIEW()
    
def TV_SCHED_CONTENT_GRAB_LINKS_PLAY(url,icon,fanart):

    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="wb-main">(.+?)</div>').findall(link)
    for links in match:
        url = re.compile ('href="(.+?)"').findall(links)[0]
        
    import urlresolver
    try:
        if urlresolver.HostedMediaFile(url).valid_url(): 
            stream_url = urlresolver.HostedMediaFile(url).resolve()
        elif liveresolver.isValid(url)==True: 
            stream_url=liveresolver.resolve(url)
        else: stream_url=url
        liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    except:
        dialog.ok(AddonTitle, "[COLOR aqua]Sorry, It seems the file has been removed at source,\nPlease try another link!\n[COLOR white]Poseidon[/COLOR]")

def TV_SEARCH():
    string =''
    keyboard = xbmc.Keyboard(string, 'Enter Search Term')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string)>1:
            term = string.lower()
            term = term.replace(' ', '%20')
            
        else: quit()
    else: term = urllib.unquote_plus(url).lower(); string = urllib.unquote_plus(url)
    url = base64.b64decode (b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9') + term
    link = open_url(url)
    match = re.compile('"series"(.+?)"series_id"').findall(link)
    for links in match:
        title = re.compile ('original_name":"(.+?)"').findall(links)[0]
        title = CLEANUP(title)
        url1 = re.compile ('"seo_name":"(.+?)"').findall(links)[0]
        url = 'http://www.watchepisodeseries.com/' + url1
        icon = 'http://www.watchepisodeseries.com/series_images/' + url1 + '.jpg'
        addDir(title,url,23,icon,fanart,'')
        
def TV_TRENDING():

    url = 'http://www.watchepisodeseries.com/'
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="trending-box">(.+?)<div class="star-point">').findall(link)
    for links in match:
        title = re.compile ('<a href=".+?" class="tb-title">(.+?)</a>').findall(links)[0].replace('Watch', '')
        title = CLEANUP(title)
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        icon = re.compile ('style="(.+?)"').findall(links)[0].replace('background-image: url(\'', '').replace('\')', '')
        addDir(title,url,23,icon,fanart,'')
        
def MAMA_HD():

    url = 'http://mamahd.com/index.html'
    link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
    match = re.compile('<div class="schedule">(.+?)<div id="pagination">').findall(link)[0]
    grab = re.compile ('<a(.+?)</a>').findall(match)
    for links in grab:
        try:
            url = re.compile ('href="(.+?)"').findall(links)[0]
            home = re.compile ('<div class="home cell">.+?<span>(.+?)</span>').findall(links)[0]
            away = re.compile ('<span>(.+?)</span>').findall(links)[1]
            comp = re.compile ('<img src="(.+?)"').findall(links)[0]
            url1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url + '%26referer=no'
            addLinkRegex(home + ' Vs ' + away,url1,2,comp,fanart)
        except:pass
        
def MOVIES_GENRES():

    url = 'https://321movies.cc/'
    link = open_url(url)
    match = re.compile('<ul class="genres scrolling">(.+?)</ul>').findall(link)[0]
    grab = re.compile ('<a href="(.+?)" title=".+?">(.+?)</a> <i>(.+?)</i>').findall(match)
    for url,title,number in grab:
        title = CLEANUP(title)
        addDir('[COLOR aqua]' + title + " :: " + 'Number of Movies ' + '[COLOR red]' + number + '[/COLOR]',url,32,icon,fanart,'')
        
def MOVIES_CONTENT(url):

    link = open_url(url)
    match = re.compile('<div class="poster">(.+?)<div class="datareviews">').findall(link)
    for links in match:
        title = re.compile ('alt="(.+?)"').findall(links)[0].replace(' For Free', '').replace('Watch ', '')
        title = CLEANUP(title)
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        icon = re.compile ('<img src="(.+?)"').findall(links)[0]
        try:
            quality = re.compile ('<span class="quality">(.+?)</span>').findall(links)[0]
        except IndexError:
            quality = 'Unknown'
        info = re.compile ('<div class="texto">(.+?)<div class="degradado">').findall(links)[0]
        addDir('[COLOR aqua]' + title + " Quality =  " + quality + '[/COLOR]',url,33,icon,fanart,info)
        
def MOVIES_LINKS(url):
    
    link = open_url(url)
    match = re.compile('<div id=".+?" class="play-box-iframe fixidtab">(.+?)</div>').findall(link)
    if not match:
        MOVIES_TVSHOWS(url)
    images = re.compile ('<div class="g-item">(.+?)</div>').findall(link)[0]
    image = re.compile ('<img src="(.+?)"').findall(images)[0]
    try:
        trailer1 = re.compile ('<div class="embed">(.+?)</iframe>').findall(link)[0]
        trailer = re.compile ('src="(.+?)"').findall(trailer1)[0]
    except IndexError:
        trailer = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    addItem('[COLOR aqua]' + "Trailer" + '[/COLOR]',trailer,666,icon,fanart,'')
    for links in match:
        url = re.compile ('src="(.+?)"').findall(links)[0]
        addLink('[COLOR aqua]'+ "Play Movie" + '[/COLOR]',url,666,icon,image,'')
        
def MOVIES_TVSHOWS(url):

    link = open_url(url)
    match = re.compile('<div class="episodiotitle">(.+?)</div>').findall(link)
    for links in match:
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        title = re.compile ('<a href=".+?">(.+?)</a>').findall(links)[0]
        addLink('[COLOR aqua]'+ title + '[/COLOR]',url,34,icon,fanarts,'')
        
def MOVIES_TVSHOWS_LINKS(url):

    link = open_url(url)
    match = re.compile('<div id=".+?" class="play-box-iframe fixidtab">(.+?)</div>').findall(link)
    for links in match:
        url = re.compile ('src="(.+?)"').findall(links)[0]
        import urlresolver
        if urlresolver.HostedMediaFile(url).valid_url(): 
            stream_url = urlresolver.HostedMediaFile(url).resolve()
        elif liveresolver.isValid(url)==True: 
            stream_url=liveresolver.resolve(url)
        else: stream_url=url
        liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setPath(stream_url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
        quit()
    
def PODCASTS_GENRES():

    url="http://podbay.fm"
    link=open_url(url)
    match=re.compile('<ul class="dropdown-menu">(.+?)</ul>',re.DOTALL).findall(link)[0]
    match2=re.compile('<li><a.+?</a></li>').findall(link)
    for item in match2:
        url1=re.compile('href="(.+?)"').findall(item)[0]
        if "http" not in url1:
            url2 = "http://podbay.fm" + url1
            title=re.compile('">(.+?)</a></li>').findall(item)[0]
            addDir(title,url2,36,icon,fanarts,'')
    
def PODCASTS_CONTENT(url):

    link=open_url(url)
    match=re.compile('<ul class="thumbnails">(.+?)</ul>',re.DOTALL).findall(link)[0]
    match2=re.compile('span3(.+?)</div></li><li',re.DOTALL).findall(match)
    for item in match2:
        title=re.compile('<h4>(.+?)</h4>').findall(item)[0]
        url1=re.compile('<a href="(.+?)">').findall(item)[0]
        if "http" not in url1:
            url2 = "http://podbay.fm" + url1
        image=re.compile('src="(.+?)"').findall(item)[0]
        addDir(title,url2,37,image,fanarts,'')
        
def PODCASTS_PLAY(url):

    link = open_url(url) 
    icon = re.compile ('<meta property="og:image" content="(.+?)"').findall(link)[0]
    match=re.compile('<div class="span8 well">(.+?)<footer style=').findall(link)[0]
    grab = re.compile ('<td>(.+?)</td>').findall(match)
    for links in grab:
        try:
            url = re.compile ('<a href="(.+?)"').findall(links)[0]
            title = re.compile ('title=".+?">(.+?)</a>').findall(links)[0]
            addLinkRegex(title,url,38,icon,fanarts,'')
        except:pass
           
def PODCASTS_PLAYREAL(url):

    link = open_url(url)
    match2 = re.compile ('<a class=\'btn btn-mini btn-primary\'(.+?)</a>').findall(link)[0]
    url = re.compile ('href=\'(.+?)\'').findall(match2)[0]
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    xbmc.Player ().play(url, liz, False)
    
         
def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'mat')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        return link
    except:quit()

def open_url2(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'mat')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
 
def get_params():
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


def addLinkMeta(name,url,mode,iconimage,itemcount,isFolder=False):
        splitName=name.partition('(')
	simplename=""
	simpleyear=""
	if len(splitName)>0:
                simplename=splitName[0]
		simpleyear=splitName[2].partition(')')
	if len(simpleyear)>0:
		simpleyear=simpleyear[0]
	mg = metahandlers.MetaData()
	meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
	liz.setInfo( type="Video", infoLabels= meta )
	contextMenuItems = []
	contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	liz.addContextMenuItems(contextMenuItems, replaceItems=False)
	if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
	else: liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
	return ok
	
def addDir(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLinkRegex(name, url, mode, iconimage, fanart, description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addLink(name, url, mode, iconimage, fanart, description=''):
    if '.ts'in url:
        url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' not in url:
        liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addItem(name,url,mode,iconimage,fanart, description=''):
    
    if '.ts'in url:
        url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty( "Fanart_Image", fanart )
    if 'plugin://' not in url:
        liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
def URL_RESOLVER(url):
    import urlresolver
    if urlresolver.HostedMediaFile(url).valid_url(): 
        stream_url = urlresolver.HostedMediaFile(url).resolve()
    elif liveresolver.isValid(url)==True: 
        stream_url=liveresolver.resolve(url)
    else: stream_url=url
    liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def SHOW_PICTURE(url):

    SHOW = "ShowPicture(" + url + ')'
    xbmc.executebuiltin(SHOW)
    sys.exit(1)
    
def CLEANUP(text):

    text = str(text)
    text = text.replace('\\r','')
    text = text.replace('\\n','')
    text = text.replace('\\t','')
    text = text.replace('\\','')
    text = text.replace('<br />','\n')
    text = text.replace('<hr />','')
    text = text.replace('&#039;',"'")
    text = text.replace('&#39;',"'")
    text = text.replace('&quot;','"')
    text = text.replace('&rsquo;',"'")
    text = text.replace('&amp;',"&")
    text = text.replace('&#8211;',"&")
    text = text.replace('&#8217;',"'")
    text = text.replace('&#038;',"&")
    text = text.replace('&nbsp;'," ")
    text = text.lstrip(' ')
    text = text.lstrip('	')

    return text

def find_single_match(text,pattern):

    result = ""
    try:    
        single = re.findall(pattern,text, flags=re.DOTALL)
        result = single[0]
    except:
        result = ""

    return result

def GetEncodeString(str):

    try:
        import chardet
        str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
    except:
        try:
            str = str.encode("utf-8")
        except:
            pass
    return str

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
	try:
	    xbmc.sleep(10)
	    retry -= 1
	    win.getControl(1).setLabel(heading)
	    win.getControl(5).setText(text)
	    return
	except:
	    pass

def view(link):
        try:
                match= re.compile('<layouttype>(.+?)</layouttype>').findall(link)[0]
                if layout=='thumbnail': xbmc.executebuiltin('Container.SetViewMode(500)')              
                else:xbmc.executebuiltin('Container.SetViewMode(50)')  
        except:pass

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanart=urllib.unquote_plus(params["fanart"])
except: pass
 
if mode==None or url==None or len(url)<1: GetMenu()
elif mode==1:GetContent(name,url,iconimage,fanart)
elif mode==2:PLAYLINK(name,url,iconimage)
elif mode==3:GETMULTI(name,url,iconimage)
elif mode==4:PLAYSD(name,url,iconimage)
elif mode==5:SEARCH()
elif mode==6:YOUTUBE_CHANNEL(url)
elif mode==7:PLAYVIDEO(url)
elif mode==8:GETMULTI_SD(name,url,iconimage)
elif mode==9:SHOW_PICTURE(url)
elif mode==10:GET_REGEX(name,url,iconimage)
elif mode==11:GET_M3U(name,url,iconimage)
elif mode==12:SCRAPE_MAMAHD(url)
elif mode==13:SCRAPE_BIGSPORTS(url)
elif mode==14:SCRAPE_MAMAHD_SPORTS_CHANNELS(url)
elif mode==15:SCRAPE_FULLHIGH()
elif mode==16:SCRAPE_FULLHIGH_GET(url,icon,fanart)
elif mode==17:resolver_settings()
elif mode==18:SCRAPE_INDI()
elif mode==19:SCRAPE_INDI_CONTENT(url)
elif mode==20:SCRAPE_INDI_LINKS(url,iconimage)
elif mode==21:TV_SCHED()
elif mode==22:TV_SCHED_CONTENT(url,name,icon,fanart)
elif mode==23:TV_SCHED_CONTENT_GRAB(url,icon,fanart)
elif mode==24:TV_SCHED_CONTENT_GRAB_LINKS(url,icon,fanart)
elif mode==25:TV_SCHED_CONTENT_GRAB_LINKS_PLAY(url,icon,fanart)
elif mode==26:TV_SEARCH()
elif mode==27:TV_TRENDING()
elif mode==28:MAMA_HD()
elif mode==29:SCRAPE_SPORTSHIGHLIGHTS_GAMES()
elif mode==30:SCRAPE_SPORTSHIGHLIGHTS_LINKS(url)
elif mode==31:MOVIES_GENRES()
elif mode==32:MOVIES_CONTENT(url)
elif mode==33:MOVIES_LINKS(url)
elif mode==34:MOVIES_TVSHOWS_LINKS(url)
elif mode==35:PODCASTS_GENRES()
elif mode==36:PODCASTS_CONTENT(url)
elif mode==37:PODCASTS_PLAY(url)
elif mode==38:PODCASTS_PLAYREAL(url)
elif mode==666:URL_RESOLVER(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))

#dialog.ok("Debug", str (match))
