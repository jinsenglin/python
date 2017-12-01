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

handler = RotatingFileHandler(app.config['APISVC_LOG'], maxBytes=10485760, backupCount=10) # 10MB per file
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(process)d - %(thread)d - %(levelname)s - %(pathname)s - %(message)s'))

app.logger.addHandler(handler)
app.logger.setLevel(app.config['APISVC_LOG_LEVEL']) # WARNING for production, DEBUG for development

# ===================== #
#                       #
# INIT TMP FOLDER       #
#                       #
# ===================== #

_process_wide_tmp_path = os.path.join(app.config['APISVC_TMP_PATH'], '{0}-{1}'.format('apisvc', os.getpid()))

if not os.path.isdir(_process_wide_tmp_path):
    os.makedirs(_process_wide_tmp_path)

# ===================== #
#                       #
# LOAD ROUTES           #
#                       #
# ===================== #

import routes
import resources

app.logger.info('apisvc is up and serving ...')
