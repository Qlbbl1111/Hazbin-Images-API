import json
import flask
from flask_restful import Resource, Api, reqparse
import random
from flask import request, jsonify


app = flask.Flask(__name__)
#app.config["DEBUG"] = True
api = Api(app)
gifs_database = open("gifs.json")

gifs = json.loads(gifs_database.read())

length = len(gifs)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hazbin Images API</h1>
<p>A silly API for fetching gifs and images I've uploaded from Hazbin Hotel/Helluva Boss shows.</p>'''


@app.route('/v1/hazbin/gif/all', methods=['GET'])
def api_all():

    return jsonify(gifs)


@app.route('/v1/hazbin/gif/random', methods=['GET'])
def api_random():

    return jsonify(gifs[random.randint(0, length)])


if __name__ == '__main__':
    app.run()