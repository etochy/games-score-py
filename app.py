import sys
from flask import Flask, json, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!Here you are in IHM adaptative API prediction."

@app.route('/asteroid-scores', methods=['POST'])
def saveScore():
    data = request.json
    return "coucou"

@app.route('/asteroid-scores', methods=['GET'])
def getScores():
    return ""

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 5000 # If you don't provide any port the port will be set to 12345

    app.run(port=port, debug=True)
