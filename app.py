import facebook
from flask import Flask
app = Flask(__name__)

@app.route('/')
def post():
	graph = facebook.GraphAPI('EAACEdEose0cBALHtWmGPrk2hzcAj5Onj2RZBZBy6zGIkNVgjvvt043VmJwCBZBLhnrGZB9YVJy6bsZCu4WgqMAxowSqLKyGurBMjCN0UjZAhI3f3GJQ8vXKDgBpziZALniCQSsx8uZCvHWFW0wH1BYdUTuIiam0nQX9D7hDz932qjAZDZD')
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

if __name__ == "__main__":
   app.run()
