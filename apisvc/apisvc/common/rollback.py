from functools import wraps
from apisvc.common.log import LOGGER


_stack = []


# def register(rescuer):
#     def register_decorator(fn):
#         @wraps(fn)
#         def wrapper(*args, **kwargs):
#
#                 # TODO put rescuer into stack
#                 _stack.append(rescuer)
#
#                 result = fn(*args, **kwargs)
#                 return result
#
#         return wrapper
#
#     return register_decorator


def register(rescuer):
    _stack.append(rescuer)


def rescue():
    while len(_stack) > 0:
        rescuer = _stack.pop()
        LOGGER.debug('poped rescuer = {0}'.format(rescuer))
