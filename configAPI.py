from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify
from flask import render_template

app = Flask(__name__)
api = Api(app)

@app.route("/", methods=['GET'])
def hello():
	d = {}
	f = open('configFile.py', 'r')
	for line in f.readlines():
		if line.startswith('#') or '=' not in line:
			continue
		# print line
		var, value = line.split('=')
		d[var.strip()] = value.rstrip().strip()
	return jsonify(d)

if __name__ == '__main__':
     app.run(host='0.0.0.0')
