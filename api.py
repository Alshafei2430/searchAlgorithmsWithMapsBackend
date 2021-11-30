from flask import Flask, jsonify
from flask_cors import CORS
import depthFirstSearchAlgo

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to the Algorithms Api'

@app.route('/test')
def testMasterPush():
    return 'this is a push from the master pranch'

@app.route('/testJSONIFY')
def testJsonify():
    return jsonify({
        "message": "test jsonify and conncet with frontend"
    })
@app.route('/depthFirstSearch')
def depthFirstSearch():
    cities = depthFirstSearchAlgo.depthFirstSearchAlgo()
    print(len(cities))
    return jsonify({"data": cities})
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)