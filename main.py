# -*- coding: utf-8 -*-
import os
import pyutilib.subprocess.GlobalData

import yaml
from flask import Flask, request, render_template, jsonify
from flaskext.markdown import Markdown

from model import optimize


with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.Loader)
pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False
app = Flask(__name__)
Markdown(app, extensions=['fenced_code'])

with open('templates/index.md', 'r') as f:
    index_content = f.read()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', mkd=index_content)
    

@app.route('/api', methods = ['POST'])
def runmodel():
    headers = request.headers
    auth = headers.get("apikey")
    if auth == config['app']['apikey']:
        data = request.get_json()
        result = optimize(data["data"], config)
        return jsonify(result), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
  
if __name__ == '__main__':
	app.run(debug=config['app']['debug'], host='0.0.0.0', port=8080)