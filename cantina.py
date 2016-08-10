import os

from settings import configs
from flask import Flask, render_template


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
#----------------------------------->>>


if __name__ == '__main__':
    app.run()
