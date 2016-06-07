#!python

from flask import Flask
from pymongo import MongoClient

app		= Flask(__name__)
client	= MongoClient()
db		= client['miniature-journey']

@app.route('/pic', methods=['POST', 'GET'])
def pic():
	if request.method == 'GET':
		pics = db.pics.find()
		return JSON.dumps(pics)
	else if request.method == 'POST':
		return JSON.dumps(request.form)
