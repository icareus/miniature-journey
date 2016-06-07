#!python

import base64
import os
import json
from flask import Flask, request
from pymongo import MongoClient

app		= Flask(__name__)
client	= MongoClient()
db		= client['miniature-journey']
updir	= os.path.dirname(os.path.realpath(__file__)) + "/uploads"
form	= 	"""
		<form method="POST" action='http://m-j.netblast.me/pic' enctype="multipart/form-data">
		<div><input type="file" name="picture"></div>
		<div><input type='text' name='title'>Title</input></div>
		<div><textarea name="description">Description</textarea></div>
		<div><input type="text" name="alt">Alt</input></div>
		<div><input type="text" name="tags">Tags</input></div>
		<button type="submit">Send it !</button>
		</form>
			"""

@app.route('/pic', methods=['POST', 'GET'])
def pic():
	res = ''
	if request.method == 'GET':
		res += form
		pics = db.pics.find()
		res += json.dumps(list(pics), indent=4, sort_keys=True)
		return res
	elif request.method == 'POST':
		res = json.dumps(request.form, indent=4, sort_keys=True)
		if 'picture' not in request.files:
			print('No file detected.')
		else:
			print('File detected: ' + request.files['picture'].filename)
			print('saving to ' + updir)
		return res
