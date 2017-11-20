import re
from functools import wraps
from flask import request, abort
from apisvc import app

PERSONATE_ADMIN = 'ADMIN'
PERSONATE_TENANT = 'TENANT'
PERSONATE_USER = 'USER'

def need_personate_header(role):
    """
        return HTTP status code 400 if there is no X-PERSONATE header in the request
        return HTTP status code 400 if there is no or wrong role specified in the value of X-PERSONATE header
        return HTTP status code 400 if the specified account id does not exist in the system
        expand **kw by injecting an object 'res_manager' if all checks are passed
    """
    def need_personate_header_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kw):
            app.logger.debug('checking X-PERSONATE header ... ')
            if 'X-PERSONATE' in request.headers:
                personation = request.headers.get('X-PERSONATE')
                if re.match(role, personation):
                    # TODO check
                    if True:
                        # TODO expand **kw
                        result = fn(*args, **kw)
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
