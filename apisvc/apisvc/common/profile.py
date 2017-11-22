import time
from functools import wraps
from apisvc.common.log import LOGGER


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        ts = time.time()
        result = fn(*args, **kw)
        te = time.time()
        LOGGER.debug('%r (%r, %r) %2.2f sec' % (fn.__name__, args, kw, te - ts))
        return result
    return wrapper
