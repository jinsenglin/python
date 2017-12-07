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

# Load default config
app.config.update(dict(
    # LOG
    APISVC_LOG='file-system',                                           #
    APISVC_LOG_PATH='/tmp',                                             # or /var/log/apisvc for production
    APISVC_LOG_NAME='apisvc.log',                                       #
    APISVC_LOG_LEVEL=logging.DEBUG,                                     # or INFO for production
    # CACHE
    APISVC_CACHE='file-system',                                         #
    APISVC_CACHE_PATH=os.path.join(app.root_path, 'cache'),             # or /var/cache/apisvc for production
    # LOCK
    APISVC_LOCK='file-system',                                          #
    APISVC_LOCK_PATH='/tmp',                                            # or /var/lock/apisvc for production
    APISVC_LOCK_NAME='apisvc.lock',                                     #
    # DB
    APISVC_DB='etcd',                                                   #
    APISVC_DB_HOST=os.environ.get('APISVC_DB_HOST', 'localhost'),       #
    # SHELL
    APISVC_SHELL_PATH=os.path.join(app.root_path, 'shell'),             #
    # TMP
    APISVC_TMP_PATH=os.path.join('/tmp'),                               # or /tmp/apisvc for production
    # MANAGER
    APISVC_MANAGERS=['cia', 'k8s', 'os'],                               #
))

# Override config from an environment variable
app.config.from_envvar('APISVC_MODE', silent=True)

#
app.config['APISVC_LOG_FILE'] = os.path.join(app.config['APISVC_LOG_PATH'], app.config['APISVC_LOG_NAME'])
app.config['APISVC_LOCK_FILE'] = os.path.join(app.config['APISVC_LOCK_PATH'], app.config['APISVC_LOCK_NAME'])
app.config['APISVC_TMP_PATH_PROC_WIDE'] = os.path.join(app.config['APISVC_TMP_PATH'], '{0}-{1}'.format('apisvc', os.getpid()))

# ===================== #
#                       #
# LOGGING SETTINGS      #
#                       #
# ===================== #

handler = RotatingFileHandler(app.config['APISVC_LOG_FILE'], maxBytes=10485760, backupCount=10) # 10MB per file
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(process)d - %(thread)d - %(levelname)s - %(pathname)s - %(message)s'))

app.logger.addHandler(handler)
app.logger.setLevel(app.config['APISVC_LOG_LEVEL']) # WARNING for production, DEBUG for development

# ===================== #
#                       #
# INIT TMP FOLDER       #
#                       #
# ===================== #

if not os.path.isdir(app.config['APISVC_TMP_PATH_PROC_WIDE']):
    os.makedirs(app.config['APISVC_TMP_PATH_PROC_WIDE'])

# ===================== #
#                       #
# LOAD ROUTES           #
#                       #
# ===================== #

import routes
import resources

app.logger.info('apisvc is up and serving ...')
