import time
from functools import wraps
from apisvc import app

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        ts = time.time()
        result = fn(*args, **kw)
        te = time.time()
        app.logger.debug('%r (%r, %r) %2.2f sec' % (fn.__name__, args, kw, te - ts))
        return result
    return wrapper
