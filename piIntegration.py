import requests
import time
from datetime import datetime
import math
import tweepy
import os
try:
	import picamera
	camera = picamera.PiCamera()
	camera.resolution =(1920,7080)
except:
	print "PiCamera not found"
''' Take an image and save it with whatever name you would like, this is not required. Time interval decides how long the shutter stays open for '''
def captureImage(intitialName,finalName,timeInterval):
	camera.capture(intitialName+'.jpg')
	time.sleep(timeInterval)
	finalName(intitialName+'.jpg',finalName) 

'''Consumer Keys and Access tokens for Twitter '''
consumer_key = configValues.Akeys['cKey']
consumer_secret = configValues.Akeys['cSec']
access_token = configValues.Atoken['atoken']
access_token_secret = configValues.Atoken['aSec']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def Tweet():
	status = "Test for twitter updates on #chennai floods at #rhok @rhok_bang"
	fn = os.path.abspath('image_stream.jpg')
	api.update_with_media(fn,status=status)
	print "tweet sent"

def restart():
	command ="/usr/bin/sudo /sbin/reboot"
	import subprocess
	process = subprocess.Popen(coommand.split(),stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print "reboot"

before_tweet = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
before_reboot = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')

while True:
	try:
		captureImage("Rishi","image_stream",60)
		after = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
		if (((after-before_tweet).seconds)/3600)==6:
			before_tweet = datetime.strptime(datetime.strftime(datetime.now(),'%H:%M:%S'),'%H:%M:%S')
			Tweet()

	except Exception,e:
		restart()
