import os
from flask import Flask

app = Flask('apisvc')

# ===================== #
#                       #
# CONFIG SETTINGS       #
#                       #
# ===================== #

#app.config.from_object(__name__)                                       # config source 1: load config from this file
#app.config.from_pyfile('application.cfg', silent=True)                 # config source 2: load config from other file

# Load default config and override config from an environment variable  # config source 3
app.config.update(dict(
    APISVC_LOG = '/tmp/apisvc.log',                                     # or /var/log/apisvc/apisvc.log
    APISVC_CACHE_STORE = os.path.join(app.root_path, 'cache'),          # or /var/cache/apisvc/accounts
    APISVC_PERSISTENT_STORE = 'localhost',                              # or remote etcd server
))

#app.config.from_envvar('APISVC_CONFIG_FILE_PATH', silent=True)         # config source 4: load config from other file

# ===================== #
#                       #
# LOGGING SETTINGS      #
#                       #
# ===================== #

import logging
app.logger.setLevel(logging.DEBUG) # WARNING for production, DEBUG for development

from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler(app.config['APISVC_LOG'], maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

#
# Basic Configuration
#
#from logging.config import dictConfig
#dictConfig({
#    'version': 1,
#    'formatters': {'default': {
#        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#    }},
#    'handlers': {'wsgi': {
#        'class': 'logging.StreamHandler',
#        'stream': 'ext://flask.logging.wsgi_errors_stream',
#        'formatter': 'default'
#    }},
#    'root': {
#        'level': 'INFO',
#        'handlers': ['wsgi']
#    }
#})

#
# Removing the Default Handler
#
#from flask.logging import default_handler
#app.logger.removeHandler(default_handler)

# ===================== #
#                       #
# LOAD ROUTES           #
#                       #
# ===================== #

import routes
