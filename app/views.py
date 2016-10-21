import os

from app import app
from flask import render_template, request

import fbconsole
from .config import FB_APP_ID

FFS_GROUP_ID = '401906879833440'

@app.route('/')

@app.route('/authorize')
def authorize_fb():
    fbconsole.APP_ID = FB_APP_ID
    fbconsole.AUTH_SCOPE = ['public_profile']
    fbconsole.authenticate()

    return "Good to go! <a href='/getposts'>Click here!</a>"

@app.route('/index')
def index():
    return render_template('index.html', app_id = os.environ.get("FB_APP_ID"))

@app.route('/group')
def group():
    # User access token expires after a couple hours; need to add login
    posts = fbconsole.get('/' + FFS_GROUP_ID + '/feed')

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

