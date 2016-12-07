#----------------------------------------
# facebook authentication
#----------------------------------------

import os

from flask import url_for, request, session, redirect, render_template, flash
from flask_oauth import OAuth, OAuthException
from app import app
from .config import *
from string_parser import parse_sale
from datetime import datetime

FFS_GROUP_ID = '401906879833440'
POST_LIMIT = 15

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
        next=url_for('group'), _external=True))

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
def group():
    try:
        fields = ['message',
                  'picture',
                  'full_picture',
                  'created_time',
                  'from',
                  'permalink_url']
        req_fields = ",".join(fields)
        posts = facebook.get(FFS_GROUP_ID + "/feed?"
                             + "fields="
                             + req_fields
                             + "&limit="
                             + str(POST_LIMIT))

        outPosts = []
        postNum = 0

        # print "posts.data", posts.data
        for post in posts.data['data']:
            # print "post", post
            msg = post.get('message')
            pic = post.get('picture')
            #print "msg", msg

            created_time = post.get('created_time')
            if created_time and msg:
                date = datetime.strptime(post['created_time'], 
                    '%Y-%m-%dT%H:%M:%S+0000')
                parsed = parse_sale(msg)
                if (parsed):
                    post['item'] = parsed['item']
                    post['price'] = parsed['price']
                    post['location'] = parsed.get('location')
                    post['description'] = parsed['description']

                    post['date'] = date.strftime('%B %d, %Y')
                    post['sortDate'] = (date - datetime.fromtimestamp(0)).total_seconds()
                    outPosts.append(post)
                    postNum += 1
        sortPosts = sorted(outPosts, key=lambda p: p['sortDate'], reverse=True)
        return render_template('group.html', posts=sortPosts)
    except OAuthException:
        flash('Authentication Error')
        return redirect(url_for('index'))
