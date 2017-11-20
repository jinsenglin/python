from flask import Flask
app = Flask('apisvc')

# ===================== #
#                       #
# CONFIG SETTINGS       #
#                       #
# ===================== #

app.config['APISVC_CONFIG_CACHE_PATH'] = 'TODO'

# ===================== #
#                       #
# LOGGING SETTINGS      #
#                       #
# ===================== #

import logging
app.logger.setLevel(logging.DEBUG) # WARNING for production, DEBUG for development

from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('/tmp/apisvc.log', maxBytes=10000, backupCount=1)
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
