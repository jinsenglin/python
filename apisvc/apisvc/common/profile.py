import time
from functools import wraps
from apisvc.common.log import LOGGER


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        LOGGER.debug('api {0} ({1}, {2}) starting'.format(fn.__name__, args, kw))
        ts = time.time()
        result = fn(*args, **kw)
        te = time.time()
        LOGGER.debug('api {0} ({1}, {2}) finished of execution time = {3} sec'.format(fn.__name__, args, kw, te - ts))
        return result
    return wrapper
