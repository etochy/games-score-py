import sys
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import json
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

max_size_data = 500

@app.route("/")
def home():
    return "Welcome!Here you are in IHM adaptative API prediction."

# Save new score
@app.route('/asteroid-scores', methods=['POST'])
@cross_origin()
def saveScore():
    scores = loadJson()
    data = request.json
    print(data)
    scores.append(data)
    scores.sort(reverse=True, key=sortScores)

    #remove data if necessary
    while len(scores) > max_size_data:
        scores.pop()

    saveJson(scores)

    return jsonify(scores)


@app.route('/asteroid-scores', methods=['GET'])
@cross_origin()
def getScores():
    scores = loadJson()
    return jsonify(scores)

def loadJson():
    jsonfile = open('./scores.json', 'r')
    new_scores = json.load(jsonfile)
    jsonfile.close()
    return new_scores

def saveJson(scores):
    jsonfile = open('./scores.json', 'w')
    json.dump(scores, jsonfile)
    jsonfile.close()
    return

def sortScores(e):
  return e['score']

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 443 # If you don't provide any port the port will be set to 12345

    app.run(port=port, debug=True)
