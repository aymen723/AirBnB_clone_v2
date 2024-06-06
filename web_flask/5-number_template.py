#!/usr/bin/python3
"""here to starts the application the web framwrok of flask.

the applicatio hear all request on port 5000 for localhost.
Routes:
     /: Hello HBNB!'.
    /hbnb: HBNB.
    /c/<text>: C with a <text> value.
    /python/(<text>): python is cool.
    /number/<n>: n but if only is integer.
    /number_template/<n>: show html page if n is integer.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """to print 'Hello HBNB!' when the request is sent"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """to print 'HBNB!' when the request is sent"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """to print C followed by a text when the request is sent"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """to print python is cool when the request is sent"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """to print n but if it's integer only when the request is sent"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """to display html page if n is integer when the request is sent"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
