#!/usr/bin/python3
"""here to starts the application the web framwrok of flask.

the applicatio hear all request on port 5000 for localhost.
Routes:
    /: Hello HBNB!'.
    /hbnb: HBNB.
    /c/<text>: C with a <text> value.
    /python/(<text>): python is cool.
    /number/<n>: n but if only is integer.
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """to print 'Hello HBNB!' when the request is sent"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """to print ' HBNB!' when the request is sent"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """to print C when the request is sent"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """to print Python is cool when the request is sent"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """to print  n only if it is integer when the request is sent"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
