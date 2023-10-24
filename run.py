#!./fight/bin/python3
from setup import loadconf
from flask import Flask


if __name__ == '__main__':
    _CONF = loadconf()
    app = Flask(__name__)
    app.debug = True