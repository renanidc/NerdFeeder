'''
	Programa python para importar feed do nerdcast
	NerdFeeder v1.0
'''

#!/usr/bin/python
# coding: utf-8

import urllib2 
from urllib2 import Request
from xml.etree.ElementTree import ElementTree

def grava_feed():
	#Importar feed da internet
	res = urllib2.urlopen('https://jovemnerd.com.br/categoria/nerdcast/feed/')

	#Gravar feed no arquivo feed.xml
	arquivo = open ('feed.xml', 'w')
	feed = res.read() #Essa leitura demora, preciso encontrar metodo mais rapido =]
	arquivo.write(feed)
	arquivo.close()


#grava_feed() #Chama funcao para importar e gravar feed

tree = ElementTree(file='feed.xml')
root = tree.getroot()

# pegar todos os link dos podcasts .mp3
for podcast in root.iter('enclosure'):  # pega todas as tags enclosure
	print podcast.tag, podcast.attrib
