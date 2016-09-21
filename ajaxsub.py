import sys
from time import time
from json import load, loads
from pprint import pprint as pp
import urllib


import pygame.mixer
from pygame.mixer import Sound,get_busy,Channel
pygame.mixer.init()



def color(x):
	return {
		'SERVICE CHANGE': 'ORANGE',
		'PLANNED WORK': 'ORANGE',
		'GOOD SERVICE':'GREEN',
		'DELAYS':'RED',
	}[x]

def add2Q(x):


	return;


def playSong(x):
	songName = "sounds/" + x.lower() + ".wav"

	print "play " + songName

	song = Sound(songName)
	
	while (get_busy() == False):
		song.play()
	return;






url  = "http://www.mta.info/service_status_json/{}".format(int(time()))

json_dict = loads(load(urllib.urlopen(url))) 

subways = json_dict['subway']['line']

mySub = [[0 for x in range(3)] for y in range(len(subways))]
x = 0

queList = []

for x in range(0,len(subways)):
	name = (subways[x]['name'])
	status = (subways[x]['status'])
	mySub[x][0] = name
	mySub[x][1] = status
	mySub[x][2] = color(status)
	fString = "Subway: " + mySub[x][0]
	print fString,
	y = len(fString)

	playSong(mySub[x][0])

	for y in range(y,16):
		sys.stdout.write(' ')
	print "Status: " + mySub[x][2]
	playSong(mySub[x][1])
	

#SERVICE CHANGE, PLANNED WORK, DELAYS, GOOD SERVICE


#f = open('output.txt','w')
#f.write(s)
#f.close()
