#!./fight/bin/python3
import logging
import time
from setup import loadconf
from back.logger import logsetup
from flask import Flask


if __name__ == '__main__':
    _CONF = loadconf()
    logreciever = logsetup(_CONF)
    ip = _CONF['GENERAL']['listen-ip']
    port = int(_CONF['GENERAL']['listen-port'])
    app = Flask(__name__)
    app.debug = True
    app.run(ip, port)