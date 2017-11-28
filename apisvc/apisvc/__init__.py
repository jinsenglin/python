import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

app = Flask('apisvc')

# ===================== #
#                       #
# CONFIG SETTINGS       #
#                       #
# ===================== #

# Load default config and override config from an environment variable
app.config.update(dict(
    APISVC_LOG='/tmp/apisvc.log',                                       # or /var/log/apisvc/apisvc.log
    APISVC_LOG_LEVEL=logging.WARNING,                                   # WARNING for production, DEBUG for development
    APISVC_CACHE='file-system',                                         # or python-object
    APISVC_CACHE_PATH=os.path.join(app.root_path, 'cache'),             # or /var/cache/apisvc/accounts
    APISVC_CACHE_LOCK='/tmp/apisvc.lock',                               # or /var/lock/apisvc/apisvc.lock
    APISVC_DB='etcd',                                                   #
    APISVC_DB_HOST='localhost',                                         #
    APISVC_SHELL_PATH=os.path.join(app.root_path, 'shell'),             #
    APISVC_TMP_PATH=os.path.join('/tmp'),                               #
    APISVC_MANAGERS=['cia', 'k8s', 'os'],                               #
))
app.config.from_envvar('APISVC_MODE', silent=True)

# ===================== #
#                       #
# LOGGING SETTINGS      #
#                       #
# ===================== #

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

handler = RotatingFileHandler(app.config['APISVC_LOG'], maxBytes=10485760, backupCount=10) # 10MB per file
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(process)d - %(thread)d - %(levelname)s - %(pathname)s - %(message)s'))
app.logger.addHandler(handler)

app.logger.setLevel(app.config['APISVC_LOG_LEVEL']) # WARNING for production, DEBUG for development

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
import resources
