from flask import flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, this is flask app'