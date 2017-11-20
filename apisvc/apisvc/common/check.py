import re
import os.path
from functools import wraps
from flask import request, abort
import etcd3
from apisvc import app
from apisvc.managers.manager import Manager
from apisvc.common import util

def _check_account_existed_in_the_persistent_store(account):
    """
        if the specified account exists in the remote persistent store
            cache it
            return True
    """

    db = app.config['APISVC_PERSISTENT_STORE']
    etcd = etcd3.client(host=db)
    value, key = etcd.get('/apisvc/accounts/{0}'.format(account))

    if key:
        credential_k8s_cache, credential_os_cache = util.credential_cache(account)

        with open(credential_k8s_cache, 'w') as k8s_file, open(credential_os_cache, 'w') as os_file:
            k8s_file.write(value);
            os_file.write(value);
            
        return True
    else:
        app.logger.debug('/apisvc/accounts/{0} not found in remote persistent store'.format(account))
        return False

def _check_account_existed(account):
    """
        return True if the specified account exists in the local cache store
        return True if the specified account exists in the remote persistent store
        return False if all checks are not passed
    """

    credential_k8s_cache, credential_os_cache = util.credential_cache(account)

    if os.path.isfile(credential_k8s_cache) and os.path.isfile(credential_os_cache):
        return True
    else:
        app.logger.debug('file {0} or {1} not found in local cache store'.format(credential_k8s_cache, credential_os_cache))
        return _check_account_existed_in_the_persistent_store(account)

PERSONATE_ADMIN = 'ADMIN'
PERSONATE_TENANT = 'TENANT'
PERSONATE_USER = 'USER'

def need_personate_header(role):
    """
        return HTTP status code 400 if there is no X-PERSONATE header in the request
        return HTTP status code 400 if there is no or wrong role specified in the value of X-PERSONATE header
        return HTTP status code 400 if the specified account does not exist in the system
        expand **kwargs by injecting an object 'apisvc_res_manager' if all checks are passed
    """
    def need_personate_header_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            app.logger.debug('checking X-PERSONATE header ... ')
            if 'X-PERSONATE' in request.headers:
                personation = request.headers.get('X-PERSONATE')
                if re.match('{0} '.format(role), personation):
                    _, account = util.personation_to_role_account(personation)
                    if _check_account_existed(account):
                        kwargs['apisvc_res_manager'] = Manager(role=role, account=account)
                        result = fn(*args, **kwargs)
                        return result
                    else:
                        app.logger.debug('bad request, no or wrong account present')
                        abort(400)
                else:
                    app.logger.debug('bad request, no or wrong role present')
                    abort(400)
            else:
                app.logger.debug('bad request, no X-PERSONATE header present')
                abort(400)
        return wrapper
    return need_personate_header_decorator
