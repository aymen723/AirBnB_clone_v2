#!/usr/bin/python3
"""here to starts the application the web framwrok of flask.

the applicatio hear all request on port 5000 for localhost.
Routes:
    /:  'Hello HBNB!'.
    /hbnb:  'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """to print 'Hello HBNB!' when the request is sent"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """to print 'HBNB!' when the request is sent"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
