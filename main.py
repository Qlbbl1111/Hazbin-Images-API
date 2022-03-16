import flask
from flask_restful import Resource, Api, reqparse
import random
from flask import request, jsonify
from gifs_database import gifs


app = flask.Flask(__name__)
#app.config["DEBUG"] = True
api = Api(app)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hazbin Images API</h1>
<p>A silly API for fetching gifs and images I've uploaded from Hazbin Hotel/Helluva Boss shows.</p>'''


@app.route('/api/v1/hazbin/all', methods=['GET'])
def api_all():
    return jsonify(gifs)


@app.route('/api/v1/hazbin/gif/random', methods=['GET'])
def api_id():

    return jsonify(gifs[random.randint(0, 3)])


if __name__ == '__main__':
    app.run()