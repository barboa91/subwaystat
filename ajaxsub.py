import sys
import urllib
import pygame.mixer
from time import time,sleep
from json import load, loads
from pprint import pprint as pp
from pygame.mixer import Sound,get_busy,Channel

pygame.mixer.init()

def color(x):
	return {
		'SERVICE CHANGE': 'ORANGE',
		'PLANNED WORK': 'ORANGE',
		'GOOD SERVICE':'GREEN',
		'DELAYS':'RED',
	}[x]

def playSong(x):
	
	songName = "sounds/" + x.lower() + ".wav"

	song = Sound(songName)
	song.play()
	
	while get_busy():
		sleep(0.01)
	
	return;

url  = "http://www.mta.info/service_status_json/{}".format(int(time()))
json_dict = loads(load(urllib.urlopen(url))) 
subways = json_dict['subway']['line']

x = 0

for x in range(0,len(subways)):
	name = (subways[x]['name'])
	status = (subways[x]['status'])

	signalColor = color(status)

	fString = "Subway: " + name
	print fString,
	playSong(name)


	y = len(fString)
	for y in range(y,16):
		sys.stdout.write(' ')
	print "Status: " + signalColor

	playSong(signalColor)
