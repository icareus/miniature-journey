#!python

import base64
import os
import json
from flask import Flask, request
from pymongo import MongoClient

app		= Flask(__name__)
client	= MongoClient()
db		= client['miniature-journey']
updir	= os.path.dirname(os.path.realpath(__file__)) + "/public/uploads"
form	= 	"""
		<form method="POST" action='http://m-j.netblast.me/pics' enctype="multipart/form-data">
		<div><input type="file" name="picture"></div>
		<div><input type='text' name='title'>Title</input></div>
		<div><textarea name="description">Description</textarea></div>
		<div><input type="text" name="alt">Alt</input></div>
		<div><input type="text" name="tags">Tags</input></div>
		<button type="submit">Send it !</button>
		</form>
			"""

def save(file, metadata):
	print('Got :')
	result = db.photos.insert_one(metadata)
	if (result.inserted_id):
		print(result.inserted_id)
		file.save(updir + "/" + str(result.inserted_id))
		metadata['id'] = str(result.inserted_id)

def get_meta(form):
	meta = {}
	for item in ('title', 'description', 'alt'):
		meta[item] = form[item][:128]
	meta['tags'] = form['tags'].split(',')
	for tag in meta['tags']:
		tag = tag.strip()
	return meta

def render_pic(db_pic):
	return('<span>' +
		'<img src="uploads/' + str(db_pic['_id']) + '" width="420" height="240">' + '</img>' +
		'<p>' + db_pic['description'] + '</p>' +
		'</span>')

@app.route('/pics', methods=['POST', 'GET'])
def pic():
	res = ''
	if request.method == 'GET':
		res += form
		for db_pic in db.photos.find():
			res += render_pic(db_pic)
		return res
	elif request.method == 'POST':
		if 'picture' not in request.files:
			return 'Uplaod error - file missing.'
		else:
			metadata = get_meta(request.form)
			save(request.files['picture'], metadata)
		return "Got upload - image ID " + metadata['id']
