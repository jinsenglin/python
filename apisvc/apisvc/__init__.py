from flask import Flask
app = Flask('apisvc')

from routes.v1 import *
