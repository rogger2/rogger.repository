#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############BIBLIOTECAS A IMPORTAR####################
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,sys,urllib,json,requests
#######################SETTINGS#########################

addon_id = 'plugin.video.brstuga'
addon_name = 'RHAFLIX'
base_url = "http://brstuga.tk/api/"
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
addondir = xbmc.translatePath(selfAddon.getAddonInfo('profile'))
artfolder = selfAddon.getAddonInfo('path')+'/resources/art/'
icon = addonfolder + '/icon.png'
fanart = addonfolder + '/fanart.jpg'
if selfAddon.getSetting('username') =='':
	xbmcgui.Dialog().ok(addon_name,'Digite seus dados de Login nas configurações...')
	selfAddon.openSettings()
username = selfAddon.getSetting('username')
password = selfAddon.getSetting('password')

###################################################MENUS############################################

def menu():
	username = selfAddon.getSetting('username')
	password = selfAddon.getSetting('password')
	status = check_user(username,password)
	if status == 'True':
		addDir('[COLOR red]•[/COLOR] Todos os Filmes','-',1,artfolder+'TELECINE PLAY.png')
		addDir('[COLOR red]•[/COLOR] Ultimos Adicionados','-',4,artfolder+'TELECINE PLAY.png')
		addDir('[COLOR red]•[/COLOR] Mais Assistidos','-',6,artfolder+'TELECINE PLAY.png')
		addDir('[COLOR red]•[/COLOR] Gêneros','-',5,artfolder+'TELECINE PLAY.png')
		addDir('[COLOR red]•[/COLOR] [COLOR blue]'+get_date().encode('utf8')+'[/COLOR]','-',00,artfolder+'ATUALIZACAO.png',False)
		addDir('[COLOR red]•[/COLOR] PicPay:\n[COLOR green]@rhalima92[/COLOR]','https://cld.pt/dl/download/dbed6e49-a814-4601-a409-5db3e903dfec/AddonPicPay.mp4',3,artfolder+'PICPAY.png',False)
		addDir('[COLOR red]•[/COLOR] Todas as Séries','-',7,artfolder+'NETFLIX.png')
		addDir('[COLOR red]•[/COLOR] Ultimas Adicionadas','-',12,artfolder+'NETFLIX.png')
		addDir('[COLOR red]•[/COLOR] Mais Assistidas','-',13,artfolder+'NETFLIX.png')
		addDir('[COLOR red]•[/COLOR] Gêneros','-',10,artfolder+'NETFLIX.png')
		addDir('[COLOR red]•[/COLOR] Creditos:\n[COLOR orange]RHa[/COLOR]','-',00,artfolder+'JESUS.png',False)
		xbmcplugin.setContent(int(sys.argv[1]), 'movies')
		xbmc.executebuiltin("Container.SetViewMode(500)")
	else:
		xbmcgui.Dialog().ok(addon_name,status,'Verifique suas configirações.')
		config()

def categorias():
	addDir('Ação','Ação',2,artfolder+'ACAO.png')
	addDir('Aventura','Aventura',2,artfolder+'AVENTURA.png')
	addDir('Animação','Animação',2,artfolder+'ANIMACAO.png')
	addDir('Biografia','Biografia',2,artfolder+'BIOGRAFIA.png')
	addDir('Comédia','Comédia',2,artfolder+'COMEDIA.png')
	addDir('Crime','Crime',2,artfolder+'CRIME.png')
	addDir('Documentário','Documentário',2,artfolder+'DOCUMENTARIO.png')
	addDir('Drama','Drama',2,artfolder+'DRAMA.png')
	addDir('Esporte','Esporte',2,artfolder+'ESPORTE.png')
	addDir('Família','Família',2,artfolder+'FAMILIA.png')
	addDir('Fantasia','Fantasia',2,artfolder+'FANTASIA.png')
	addDir('História','História',2,artfolder+'HISTORIA.png')
	addDir('Gospel','Gospel',2,artfolder+'GOSPEL.png')
	addDir('Terror','Terror',2,artfolder+'TERROR.png')
	addDir('Música','Música',2,artfolder+'MUSICA.png')
	addDir('Mistério','Mistério',2,artfolder+'MISTERIO.png')
	addDir('Nacional','Nacional',2,artfolder+'NACIONAL.png')
	addDir('Romance','Romance',2,artfolder+'ROMANCE.png')
	addDir('Ficção científica','Ficção científica',2,artfolder+'FICCAO CIENTIFICA.png')
	addDir('Artistas','Artistas',2,artfolder+'ARTISTA.png')
	addDir('Suspense','Suspense',2,artfolder+'SUSPENSE.png')
	addDir('Guerra','Guerra',2,artfolder+'GUERRA.png')
	addDir('Faroeste','Faroeste',2,artfolder+'FAROESTE.png')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(500)")
	
def categorias_tvshows():
	addDir('Ação','Ação',11,artfolder+'ACAO.png')
	addDir('Aventura','Aventura',11,artfolder+'AVENTURA.png')
	addDir('Animação','Animação',11,artfolder+'ANIMACAO.png')
	addDir('Biografia','Biografia',11,artfolder+'BIOGRAFIA.png')
	addDir('Comédia','Comédia',11,artfolder+'COMEDIA.png')
	addDir('Crime','Crime',11,artfolder+'CRIME.png')
	addDir('Documentário','Documentário',11,artfolder+'DOCUMENTARIO.png')
	addDir('Drama','Drama',11,artfolder+'DRAMA.png')
	addDir('Esporte','Esporte',11,artfolder+'ESPORTE.png')
	addDir('Família','Família',11,artfolder+'FAMILIA.png')
	addDir('Fantasia','Fantasia',11,artfolder+'FANTASIA.png')
	addDir('História','História',11,artfolder+'HISTORIA.png')
	addDir('Gospel','Gospel',11,artfolder+'GOSPEL.png')
	addDir('Terror','Terror',11,artfolder+'TERROR.png')
	addDir('Música','Música',11,artfolder+'MUSICA.png')
	addDir('Mistério','Mistério',11,artfolder+'MISTERIO.png')
	addDir('Nacional','Nacional',11,artfolder+'NACIONAL.png')
	addDir('Romance','Romance',11,artfolder+'ROMANCE.png')
	addDir('Ficção científica','Ficção científica',11,artfolder+'FICCAO CIENTIFICA.png')
	addDir('Artistas','Artistas',11,artfolder+'ARTISTA.png')
	addDir('Suspense','Suspense',11,artfolder+'SUSPENSE.png')
	addDir('Guerra','Guerra',11,artfolder+'GUERRA.png')
	addDir('Faroeste','Faroeste',11,artfolder+'FAROESTE.png')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin("Container.SetViewMode(500)")
	
def get_movies():
	adult = get_parental()
	code = requests.get(base_url + "%s/%s/movies/" % (username, password)).text
	json_data = json.loads(code)
	for filme in json_data:
		idd = filme['id']
		tmdb_id =filme['tmdb_id']
		url = filme['url']
		title = filme['title']
		poster_path = filme['poster_path']
		backdrop_path = filme['backdrop_path']
		overview = filme['overview']
		release_date = filme['release_date']
		vote_average = filme['vote_average']
		genres = filme['genres']
		trailer = filme['trailer']
		parental = filme['parental']
		cast = filme['cast']
		link = base_url + "%s/%s/player/%s/%s/%s/" % (username, password,'filme',idd,setQuality())
		if parental < 18:
			if parental == 0:
				parental = 'Livre'
			else:
				parental = str(parental)+' Anos'
			dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
			addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
		else:
			if adult == selfAddon.getSetting('parental'):
				parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')	
	xbmc.executebuiltin('Container.SetViewMode(51)')
	
def get_movies_last():
	adult = get_parental()
	code = requests.get(base_url + "%s/%s/movies/last/" % (username, password)).text
	json_data = json.loads(code)
	for filme in json_data:
		idd = filme['id']
		tmdb_id =filme['tmdb_id']
		url = filme['url']
		title = filme['title']
		poster_path = filme['poster_path']
		backdrop_path = filme['backdrop_path']
		overview = filme['overview']
		release_date = filme['release_date']
		vote_average = filme['vote_average']
		genres = filme['genres']
		trailer = filme['trailer']
		parental = filme['parental']
		cast = filme['cast']
		link = base_url + "%s/%s/player/%s/%s/%s/" % (username, password,'filme',idd,setQuality())
		if parental < 18:
			if parental == 0:
				parental = 'Livre'
			else:
				parental = str(parental)+' Anos'
			dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
			addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
		else:
			if adult == selfAddon.getSetting('parental'):
				parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')	

def get_movies_popular():
	adult = get_parental()
	code = requests.get(base_url + "%s/%s/movies/popular/" % (username, password)).text
	json_data = json.loads(code)
	for filme in json_data:
		idd = filme['id']
		tmdb_id =filme['tmdb_id']
		url = filme['url']
		title = filme['title']
		poster_path = filme['poster_path']
		backdrop_path = filme['backdrop_path']
		overview = filme['overview']
		release_date = filme['release_date']
		vote_average = filme['vote_average']
		genres = filme['genres']
		trailer = filme['trailer']
		parental = filme['parental']
		cast = filme['cast']
		link = base_url + "%s/%s/player/%s/%s/%s/" % (username, password,'filme',idd,setQuality())
		if parental < 18:
			if parental == 0:
				parental = 'Livre'
			else:
				parental = str(parental)+' Anos'
			dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
			addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
		else:
			if adult == selfAddon.getSetting('parental'):
				parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
def get_movies_genre(url):
	adult = get_parental()
	cat = url.decode('utf8')
	code = requests.get(base_url + "%s/%s/movies/" % (username, password)).text
	json_data = json.loads(code)
	for filme in json_data:
		genres = filme['genres']
		if cat in genres:
			idd = filme['id']
			tmdb_id =filme['tmdb_id']
			title = filme['title']
			url = filme['url']
			poster_path = filme['poster_path']
			backdrop_path = filme['backdrop_path']
			overview = filme['overview']
			release_date = filme['release_date']
			vote_average = filme['vote_average']
			trailer = filme['trailer']
			parental = filme['parental']
			cast = filme['cast']
			link = base_url + "%s/%s/player/%s/%s/%s/" % (username, password,'filme',idd,setQuality())
			if parental < 18:
				if parental == 0:
					parental = 'Livre'
				else:
					parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
			else:
				if adult == selfAddon.getSetting('parental'):
					parental = str(parental)+' Anos'
					dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
					addDir4(title.encode('utf8'),link,3,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,trailer,False)
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(51)')

def get_tvshows():
	adult = get_parental()
	code = requests.get(base_url + "%s/%s/tvshows/" % (username, password)).text
	json_data = json.loads(code)
	for serie in json_data:
		idd = serie['id']
		tmdb_id = serie['tmdb_id']
		title = serie['title']
		poster_path = serie['poster_path']
		backdrop_path = serie['backdrop_path']
		overview = serie['overview']
		release_date = serie['release_date']
		vote_average = serie['vote_average']
		genres = serie['genres']
		parental = serie['parental']
		cast = serie['cast']
		if parental < 18:
			if parental == 0:
				parental = 'Livre'
			else:
				parental = str(parental)+' Anos'
			dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
			addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
		else:
			if adult == selfAddon.getSetting('parental'):
				parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')	
	xbmc.executebuiltin('Container.SetViewMode(51)')	
	
def get_tvshows_genre(url):
	adult = get_parental()
	cat = url.decode('utf8')
	code = requests.get(base_url + "%s/%s/tvshows/" % (username, password)).text
	json_data = json.loads(code)
	for serie in json_data:
		genres = serie['genres']
		if cat in genres:
			idd = serie['id']
			tmdb_id = serie['tmdb_id']
			title = serie['title']
			poster_path = serie['poster_path']
			backdrop_path = serie['backdrop_path']
			overview = serie['overview']
			release_date = serie['release_date']
			vote_average = serie['vote_average']
			parental = serie['parental']
			cast = serie['cast']
			if parental < 18:
				if parental == 0:
					parental = 'Livre'
				else:
					parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
			else:
				if adult == selfAddon.getSetting('parental'):
					parental = str(parental)+' Anos'
					dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
					addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')	
	xbmc.executebuiltin('Container.SetViewMode(51)')

def get_tvshows_last():
	adult = get_parental()
	code = requests.get(base_url + "%s/%s/tvshows/last/" % (username, password)).text
	json_data = json.loads(code)
	for serie in json_data:
		idd = serie['id']
		tmdb_id = serie['tmdb_id']
		title = serie['title']
		poster_path = serie['poster_path']
		backdrop_path = serie['backdrop_path']
		overview = serie['overview']
		release_date = serie['release_date']
		vote_average = serie['vote_average']
		genres = serie['genres']
		parental = serie['parental']
		cast = serie['cast']
		if parental < 18:
			if parental == 0:
				parental = 'Livre'
			else:
				parental = str(parental)+' Anos'
			dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
			addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
		else:
			if adult == selfAddon.getSetting('parental'):
				parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')	
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
def get_tvshows_popular():
	adult = get_parental()
	code = requests.get(base_url + "%s/%s/tvshows/popular/" % (username, password)).text
	json_data = json.loads(code)
	for serie in json_data:
		idd = serie['id']
		tmdb_id = serie['tmdb_id']
		title = serie['title']
		poster_path = serie['poster_path']
		backdrop_path = serie['backdrop_path']
		overview = serie['overview']
		release_date = serie['release_date']
		vote_average = serie['vote_average']
		genres = serie['genres']
		parental = serie['parental']
		cast = serie['cast']
		if parental < 18:
			if parental == 0:
				parental = 'Livre'
			else:
				parental = str(parental)+' Anos'
			dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
			addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
		else:
			if adult == selfAddon.getSetting('parental'):
				parental = str(parental)+' Anos'
				dados = '\n\n[B]Classificação Indicativa: [COLOR=red]'+parental+'[/COLOR]\nAtores: [COLOR=red]'+str(cast.encode('utf8'))+'[/COLOR] [/B]'
				addDir3(title.encode('utf8'),str(idd),8,poster_path,backdrop_path,overview.encode('utf8')+dados,release_date,genres,vote_average,'')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')	
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
def get_seasons(name,url,iconimage):
	code = requests.get(base_url + "%s/%s/tvshows/%s/" % (username, password,url)).text
	json_data = json.loads(code)
	for temporada in json_data:
		temporada = temporada['id']
		addDir3('Temporada '+str(temporada),url,9,iconimage,'-',"Selecione a Temporada:",'-','-','-','')
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(55)')
		
def get_episodes(name,url):
	idd_tv = name.split(' ')
	code = requests.get(base_url + "%s/%s/tvshows/%s/%s/" % (username, password, url, idd_tv[1])).text
	json_data = json.loads(code)
	for episodio in json_data:
		idd = episodio['id']
		tvshow = episodio['tvshow']
		season = episodio['season']
		number = episodio['number']
		title = episodio['title']
		overview = episodio['overview']
		still_path = episodio['still_path']
		vote_average = episodio['vote_average']
		air_date = episodio['air_date']
		link = base_url + "%s/%s/player/%s/%s/%s/" % (username, password,'serie',idd,setQuality())
		title = '[COLOR blue]T'+str(season)+'E'+str(number)+'[/COLOR] '+title.encode('utf8')
		addDir4(title,link,3,still_path,'backdrop_path',overview.encode('utf8'),air_date,'',vote_average,'',False)
	
def Player(name,url,iconimage):
	playlist = xbmc.PlayList(0)
	playlist.clear()
	listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
	listitem.setInfo("Video", {"Title":name})
	listitem.setProperty('mimetype', 'video/mp4')
	playlist.add(str(url),listitem)
	xbmcPlayer = xbmc.Player()
	xbmcPlayer.play(playlist)

##############################################################################################################
##											FUNÇÕES															##
##############################################################################################################
def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+ "&iconimage=" + urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
def addDir3(name,url,mode,iconimage,art,description,year,genre,nota,trailer,pasta=True,total=1):
	sysaddon = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+ "&iconimage=" + urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="iconimage", thumbnailImage=iconimage)
	liz.setArt({'poster':iconimage,'banner':art})
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Rating": nota, "Genre": genre, "Year": year, "Trailer": 'plugin://plugin.video.youtube/play/?video_id='+trailer})
	liz.setProperty("fanart_image", art)	
	contextMenuItems = []
	contextMenuItems.append(("Informações", "XBMC.Action(Info)","RunPlugin(%s?action=addView&content=movies)" % sysaddon))
	liz.addContextMenuItems(contextMenuItems, replaceItems=False)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=sysaddon,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
def addDir4(name,url,mode,iconimage,art,description,year,genre,nota,trailer,pasta=True,total=1):
	sysaddon = sys.argv[0]
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="iconimage", thumbnailImage=iconimage)
	liz.setArt({'poster':iconimage,'banner':art})
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Rating": nota, "Genre": genre, "Year": year, "Trailer": 'plugin://plugin.video.youtube/play/?video_id='+trailer})
	liz.setProperty("fanart_image", art)	
	contextMenuItems = []
	contextMenuItems.append(("Informações", "XBMC.Action(Info)","RunPlugin(%s?action=addView&content=movies)" % sysaddon))
	liz.addContextMenuItems(contextMenuItems, replaceItems=False)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
def check_user(username,password):
    code = requests.get(base_url+"%s/%s/"%(username,password)).text
    return code
def get_date():
	code = requests.get(base_url+"%s/%s/configs/"%(username,password)).text
	json_data = json.loads(code)
	date = json_data[0]['update']
	date = date.split('-')
	date = '%s/%s/%s'%(date[2],date[1],date[0])
	return date
def get_parental():
	code = requests.get(base_url+"%s/%s/configs/"%(username,password)).text
	json_data = json.loads(code)
	return json_data[0]['parental']
def config():
	selfAddon.openSettings()
	return menu()
def setQuality():
	quality = selfAddon.getSetting('quality')
	if quality == '0':
		return 'm22'
	else:
		return 'm18'
############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################             
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
params=get_params()
url=None
name=None
mode=None
iconimage=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################
if mode==None or url==None or len(url)<1:
	menu()	
elif mode==1:
	get_movies()
elif mode==2:
	get_movies_genre(url)
elif mode==3:
	Player(name,url,iconimage)	
elif mode==4:
	get_movies_last()
elif mode==5:
	categorias()
elif mode==6:
	get_movies_popular()
elif mode==7:
	get_tvshows()
elif mode==8:
	get_seasons(name,url,iconimage)
elif mode==9:
	get_episodes(name,url)
elif mode==10:
	categorias_tvshows()
elif mode==11:
	get_tvshows_genre(url)	
elif mode==12:
	get_tvshows_last()
elif mode==13:
	get_tvshows_popular()
elif mode==14:
	config()
xbmcplugin.endOfDirectory(int(sys.argv[1]))