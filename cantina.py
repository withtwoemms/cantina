from __future__ import print_function

import json
import os
import requests
import sys

from settings import configs
from flask import Flask, jsonify, render_template, request


env = os.environ.get('FLASK_APP_ENV', 'default')
app = Flask(__name__)

#-- CONFIG -------------------------->>>
app.config.from_object(configs[env])
#----------------------------------->>>

#-- VIEWS -------------------------->>>
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World"

@app.route('/outside/<posts>', defaults={'num': None}, methods=['GET'])
@app.route('/outside/<posts>/<int:num>', methods=['GET'])
def outside(posts, num):
    if posts == 'posts':
        url = 'https://jsonplaceholder.typicode.com/{}'.format(posts)
    if posts == 'posts' and num:
        url = 'https://jsonplaceholder.typicode.com/{}/{}'.format(posts, num)
    response = requests.get(url)
    return json.dumps({
        'url': url,
        'status': response.status_code,
        'response': response.json(),
    })
#---------------------------------->>>


if __name__ == '__main__':
    app.run()
