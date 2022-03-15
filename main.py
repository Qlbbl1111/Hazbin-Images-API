import flask
import random
from flask import request, jsonify
from gifs_database import gifs


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/hazbin/all', methods=['GET'])
def api_all():
    return jsonify(gifs)


@app.route('/api/v1/hazbin/gif/random', methods=['GET'])
def api_id():

    return jsonify(gifs[random.randint(0, 3)])

app.run()