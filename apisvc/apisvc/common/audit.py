from functools import wraps
from apisvc.common.log import LOGGER


def audit_anonymous_access(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        LOGGER.info('anonymous requests api {0} ({1}, {2})'.format(fn.__name__, args, kwargs))
        result = fn(*args, **kwargs)
        return result

    return wrapper


def audit_access(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        LOGGER.info('{0} requests api {1} ({2}, {3})'.format(kwargs['apisvc_res_manager'], fn.__name__, args, kwargs))
        result = fn(*args, **kwargs)
        return result

    return wrapper
