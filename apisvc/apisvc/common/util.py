import os
import thread
import yaml
import calendar
import time
import random
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER


_tmp_path = CONFIG['APISVC_TMP_PATH']


def get_ptt_string():
    """
        ptt is short for process-thread-timestamp
    """
    return '{0}-{1}-{2}'.format(os.getpid(), thread.get_ident(), calendar.timegm(time.gmtime()))


def get_process_wide_tmp_path():
    return os.path.join(_tmp_path, str(os.getpid()))


def parse_os_credential(os_credential_path):
    region_name = None
    auth_url = None
    username = None
    password = None
    project_name = None

    with open(os_credential_path, 'r') as stream:
        try:
            data = yaml.load(stream)
            region_name = data['clouds']['os']['region_name']
            auth_url = data['clouds']['os']['auth']['auth_url']
            username = data['clouds']['os']['auth']['username']
            password = data['clouds']['os']['auth']['password']
            project_name = data['clouds']['os']['auth']['project_name']
        except yaml.YAMLError:
            LOGGER.critical('failed to parse os credential')

    return region_name, auth_url, username, password, project_name

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
