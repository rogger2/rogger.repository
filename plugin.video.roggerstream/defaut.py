#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,base64,xmltosrt,os
from BeautifulSoup import BeautifulSoup
h = HTMLParser.HTMLParser()


versao = '1.0.8'
addon_id = 'plugin.video.roggerstream'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.png'
 

###################################################MENUS############################################

	
def  menus():        		
	dialog = xbmcgui.Dialog()
	dialog.ok("ROGGER STREAM", "          Assistam a vários canais IPTV do Brasil e do mundo !!!")
	addDir('ROGGER STREAM','-',3,'http://todanovidade.com.br/wp-content/gallery/tv-gratis/tv-gratis-13.jpg')
	
	

def  categorias():
	addDir('CANAIS ABERTOS DO BRASIL','https://copy.com/Nlyj6xxWlRFKdinh?download=1',6,'http://tvfoco.pop.com.br/audiencia/wp-content/uploads/2013/07/Emissoras-sp-globo-record-sbt-band-redetv-cultura-e10audiencia-474x316.jpg')
	addDir('TV PAGA','-',5,'http://i.ytimg.com/vi/QdrmV91uNn0/maxresdefault.jpg')
	addDir('CANAIS LATINOS','https://copy.com/tapliy8nIaKSLDQq?download=1',6,'http://www.adquieralo.com/imagenes/banderas-latinas.png')
	addDir('CANAIS DE PORTUGAL','https://copy.com/unoGFK2bL8ZJ0iHD?download=1',6,'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTJDrJdCWYyLDMVxdvWQ5SMqDCB6C59_RWBZbxahkzrYVAECA_j_Q')
	addDir('WEBCAMS','https://copy.com/Ywh4MnZQqy2R7M8P?download=1',6,'https://cdn2.iconfinder.com/data/icons/communication-14/512/Webcam-512.png')
	addDir('CANAIS HD','https://copy.com/VMoOgU8UDvAgfjv0?download=1',6,'http://www.weddingsipa.com/images/new_hd_logo.jpg')
	addDir('MÚSICAS E VIDEOCLIPES','https://copy.com/1cvRyOdMSOCSBH70?download=1',6,'http://www.aitechautomacao.com.br/images/musica.png')
	addDir('ESPORTES INTERNACIONAIS','https://copy.com/bIIpBHwFbXMXOBBB?download=1',6,'http://s.glbimg.com/es/ge/f/original/2012/03/05/mascote_esporte_todos.jpg')
	addDir('RÁDIOS','https://copy.com/znUclLey0qF30gSd?download=1',6,'http://s.glbimg.com/po/tt/f/original/2013/10/21/011787436-radio-station-microphone.jpeg')
	
	


def  categorias_tv_paga():
	addDir('CAÇA E PESCA','https://copy.com/b6uCi8jKTmq24wLy?download=1',6,'')
	addDir('SÉRIES E DESENHOS 24 HORAS','https://copy.com/nEagWXhOC1s7dlyO?download=1',6,'')
	addDir('DOCUMENTÁRIOS','https://copy.com/u3fZuJaCSqXQUNuk?download=1',6,'')
	addDir('ESPORTES','https://copy.com/342Ys8apG9i2Ar9J?download=1',6,'')	
	addDir('FILMES E SÉRIES','https://copy.com/qaC2wr0YHQ3cWgN3?download=1',6,'')
	addDir('INFANTIL','https://copy.com/FH28QXuLwrJY9cXS?download=1',6,'')	
	addDir('NOTÍCIAS','https://copy.com/r19WdvfFW4xP7h7Q?download=1',6,'')
	addDir('RELIGIOSOS','https://copy.com/S6Jm2vh2DYJDTEwJ?download=1',6,'')
	addDir('VARIEDADES','https://copy.com/DUKhtoZqYdjklcOa?download=1',6,'')	
	
	
def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")
	  
	  
def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

def addDir(name,url,mode,iconimage,pasta=True,total=1):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok
	
	
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


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)


###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode==None or url==None or len(url)<1:
    print ""
    menus()
	
elif mode==3:
	print ""
	categorias()

elif mode==5:
	print ""
	categorias_tv_paga()	
	
elif mode==6: 
	print ""
	listar_canais(url)

	

	


	
xbmcplugin.endOfDirectory(int(sys.argv[1]))
