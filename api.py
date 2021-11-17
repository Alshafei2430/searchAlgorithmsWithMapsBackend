from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Algorithms Api'

@app.route('/test')
def testMasterPush():
    return 'this is a push from the master pranch'
