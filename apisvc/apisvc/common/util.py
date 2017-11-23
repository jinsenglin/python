import time
import random
from apisvc.common.log import LOGGER


def personation_to_role_account(personation):
    return tuple(personation.split(' '))


def simulate_time_consuming_op(seconds=None):
    if seconds is not None:
        LOGGER.debug('.......................down {0} seconds'.format(seconds))
        time.sleep(seconds)
    else:
        seconds = random.uniform(1, 10)
        LOGGER.debug('.......................down {0} seconds'.format(seconds))
        time.sleep(seconds)

    LOGGER.debug('...........................up')
