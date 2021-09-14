#!/usr/bin/env python


import sys
import os
import time
from twython import Twython, TwythonError
from datetime import datetime
import pytz

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']
TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21


today = datetime.now()
tz = pytz.timezone('Asia/Manila') # change the timezone to your desired/home timezone.
pht = datetime.now(tz) #change the variable too if you want

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('./output/shop.png', 'rb')


tweetStr = 'Fortnite item shop for '+pht.strftime("%m/%d/%y")+'!\n'+pht.strftime("%I:%M %p")+', PHT/GMT+8\n\nIf you want to support me, make sure to use code \"GK\" on the Fortnite Item Shop!\nReally appreciate it!'

api = twitter_handle()
response = api.upload_media(media=photo)
api.update_status(status=tweetStr, media_ids=[response['media_id']])

print ("Tweeted: " + tweetStr)
