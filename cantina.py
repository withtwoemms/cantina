import json
import os
import requests

from settings import configs
from flask import Flask, render_template, request


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

@app.route('/outside', methods=['GET'])
def outside():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return json.dumps({
        'url': 'https://jsonplaceholder.typicode.com/posts',
        'status': response.status_code,
        'response': response.content,
    })
#----------------------------------->>>


if __name__ == '__main__':
    app.run()
