#!python

import json
from flask import Flask, request
from pymongo import MongoClient

app		= Flask(__name__)
client	= MongoClient()
db		= client['miniature-journey']

@app.route('/pic', methods=['POST', 'GET'])
def pic():
	if request.method == 'GET':
		pics = db.pics.find()
		return json.dumps(pics)
	elif request.method == 'POST':
		return json.dumps(request.form)
