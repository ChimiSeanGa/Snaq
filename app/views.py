import os

from app import app
from flask import render_template

from facebook import get_user_from_cookie, GraphAPI
from .config import FB_APP_ID

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', app_id = os.environ.get("FB_APP_ID"))

@app.route('/group')
def group():
    # User access token expires after a couple hours; need to add login
    graph = GraphAPI('EAACEdEose0cBALHtWmGPrk2hzcAj5Onj2RZBZBy6zGIkNVgjvvt043VmJwCBZBLhnrGZB9YVJy6bsZCu4WgqMAxowSqLKyGurBMjCN0UjZAhI3f3GJQ8vXKDgBpziZALniCQSsx8uZCvHWFW0wH1BYdUTuIiam0nQX9D7hDz932qjAZDZD')
    ffs_group_id = '401906879833440'
    ip_group_id = '341686389286734'

    posts = graph.get_object(ffs_group_id + '/feed')

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

