import re
import os.path
from functools import wraps
from flask import request, abort
from apisvc import app

def _check_account_existed(personation):
    """
        return True if the specified account exists in the local cache store
        return True if the specified account exists in the remote persistent store
        return False if all checks are not passed
    """

    pair = personation.split(' ')
    if (len(pair) < 2):
        app.logger.debug('account not present')
        return False
    else:
        account = pair[1]
        account_k8s = '{0}.k8s.yaml'.format(account)
        account_os = '{0}.os.yaml'.format(account)

        cache = app.config['APISVC_CACHE_STORE']
        account_k8s_cache = '{0}/{1}'.format(cache, account_k8s)
        account_os_cache = '{0}/{1}'.format(cache, account_os)

        if os.path.isfile(account_k8s_cache) and os.path.isfile(account_os_cache):
                return True
        else:
            app.logger.debug('file {0} or {1} not found'.format(account_k8s_cache, account_os_cache))
            # TODO check remote persistent store
            return False

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
                if re.match(role, personation):
                    if _check_account_existed(personation):
                        # TODO expand **kwargs
                        kwargs['apisvc_res_manager'] = 'TODO'
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
