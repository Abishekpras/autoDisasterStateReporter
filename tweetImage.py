''' Code by Rishi Gaurav Bhatnagar, because he is lazy and he likes to tweet, FAST'''
#!/usr/bin/env python2.7

import tweepy
import sys
import configValues
import os

# Consumer keys and access tokens, used for OAuth
consumer_key = configValues.Akeys['cKey']
consumer_secret = configValues.Akeys['cSec']
access_token = configValues.Atoken['atoken']
access_token_secret = configValues.Atoken['aSec']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def tweetNow():

    status = "Test for twitter updates on #chennai floods at #rhok @rhok_bang"
    fn = os.path.abspath("imageName.jpg")

    api.update_with_media(fn,status=status)
    print "tweet sent"


tweetNow()
