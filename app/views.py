import os

from app import app
from flask import render_template, request
import urllib2, json

import fbconsole
# from .config import FB_APP_ID, FFS_GROUP_ID

FFS_GROUP_ID = '401906879833440'
FB_GRAPH = 'https://graph.facebook.com/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/authorize')
def authorize_fb():
    fbconsole.APP_ID = '1821863698046613'
    fbconsole.AUTH_SCOPE = ['public_profile']
    fbconsole.authenticate()

    return render_template('authorize.html')

@app.route('/group')
def getposts():
    posts = json.loads(urllib2.urlopen(FB_GRAPH + FFS_GROUP_ID + 
        "/feed?access_token=" + fbconsole.ACCESS_TOKEN + 
        "&fields=message,picture").read())

    postNum = 1
    curPost = ''

    for post in posts['data']:
        curPost += '<br>POST #' + str(postNum) + '<br>'
        
        curPost += post['message']

        curPost += '<br>'

        try:
            curPost += '<img src="' + post['picture'] + '">'
        except KeyError:
            curPost += 'No picture included'

        curPost += '<br>'
        postNum += 1

    return curPost

