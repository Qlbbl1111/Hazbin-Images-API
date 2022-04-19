import json
import flask
from flask_restful import Resource, Api, reqparse
import random
import json
from flask import request
from flask import jsonify

app = flask.Flask(__name__)
#app.config["DEBUG"] = True
api = Api(app)
gifs_database = open("gifs.json")

gifs = json.loads(gifs_database.read())

length = len(gifs)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

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


@app.route('/v1/swim', methods=['POST'])
def process_form():
    data = request.form
    swimdata = data['swim']
    print(swimdata)
    if swimdata.lower() == 'true':
        x = "true"
        with open(f'swim.json', 'w') as f:
            f.write(f"{{\"isswim\":{x}}}")
    elif swimdata.lower() == 'false':
        x = "false"
        with open(f'swim.json', 'w') as f:
            f.write(f"{{\"isswim\":{x}}}")
    else:
        pass
    with open(f'swim.json', 'r') as f:
        y = f.read()
        z = json.loads(y)
        j = z.get("isswim")
    return str(j)



if __name__ == '__main__':
    app.run()