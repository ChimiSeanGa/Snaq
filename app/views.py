#----------------------------------------
# facebook authentication
#----------------------------------------

import os

from flask import url_for, request, session, redirect, render_template
from flask_oauth import OAuth
from app import app
from .config import *

FFS_GROUP_ID = '401906879833440'

""" FACEBOOK AUTHENTICATION """
oauth = OAuth()
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FB_APP_ID,
    consumer_secret=FB_APP_SECRET,
    #request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    return redirect(next_url)

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))
""" END FACEBOOK AUTHENTICATION """

@app.route('/group')
def getposts():
    posts = facebook.get(FFS_GROUP_ID + '/feed?fields=message,picture')

    outPosts = []
    postNum = 0

    # print "posts.data", posts.data
    for post in posts.data['data']:
        # print "post", post

        try:
            msg = post['message']
        except KeyError:
            msg = 'NMS'

        try:
            pic = post['picture']
        except KeyError:
            pic = 'NPI'

        if (msg != 'NMS' and pic != 'NPI'):
            outPosts.append({'message': msg, 'picture': pic})
            postNum += 1
    return render_template('group.html', posts=outPosts)
