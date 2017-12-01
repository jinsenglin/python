import yaml
import time
import random
from apisvc.common.log import LOGGER


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
