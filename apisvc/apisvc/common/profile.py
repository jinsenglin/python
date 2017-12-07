import time
from functools import wraps
from apisvc.common.log import LOGGER


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """measure execution time in microseconds

        Args:
            *args:
            **kw:

        Returns:

        """
        LOGGER.debug('api {0} ({1}, {2}) starting'.format(fn.__name__, args, kwargs))
        ts = time.time()
        result = fn(*args, **kwargs)
        te = time.time()
        LOGGER.info('api {0} ({1}, {2}) finished of execution time = {3:.6f} sec'.format(fn.__name__, args, kwargs, te - ts))
        return result
    return wrapper
