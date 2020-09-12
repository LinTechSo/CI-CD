#!/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

#dynamic route
@app.route('/hello/<username>')
def hello_user(username):
    return 'Why Hello %s!\n' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0')

