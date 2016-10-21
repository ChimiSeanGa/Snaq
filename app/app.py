import fbconsole
import flask
from flask import Flask, abort, request
app = Flask(__name__)

FFS_GROUP_ID = '401906879833440'
APP_ID = '1821863698046613'

@app.route('/authorize')
def authorize_facebook():
	fbconsole.APP_ID = APP_ID
	fbconsole.AUTH_SCOPE = ['public_profile']
	fbconsole.authenticate()

	return "Good to go! <a href='/getposts'>Click here!</a>"

@app.route('/')
def home():
	# User access token expires after a couple hours; need to add login

	return '<a href="/authorize">Login</a>'

@app.route('/getposts')
def getposts():
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

if __name__ == "__main__":
   app.run()
