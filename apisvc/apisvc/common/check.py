from functools import wraps
from apisvc import app

PERSONATE_ADMIN = 'ADMIN'
PERSONATE_TENANT = 'TENANT'
PERSONATE_USER = 'USER'

def need_personate_header(role):
    def need_personate_header_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kw):
            app.logger.debug('checking X-PERSONATE header ...')
            result = fn(*args, **kw)
            return result
        return wrapper
    return need_personate_header_decorator
