import os
import thread
import yaml
import calendar
import time
import random
from apisvc.common.config import CONFIG
from apisvc.common.log import LOGGER


_tmp_path = CONFIG['APISVC_TMP_PATH']


def native_k8s_user_object_to_ring_credential(k8s_controller, k8s_user):
    # TODO
    LOGGER.debug('k8s_controller = {0}'.format(k8s_controller))
    LOGGER.debug('k8s_user = {0}'.format(k8s_user))
    return k8s_user


def native_os_user_object_to_ring_credential(os_controller, os_user):
    # TODO
    LOGGER.debug('os_controller = {0}'.format(os_controller))
    LOGGER.debug('os_user = {0}'.format(os_user))
    return os_user


def get_ptt_string():
    """
        ptt is short for process-thread-timestamp
    """
    return 'apisvc-{0}-{1}-{2}'.format(os.getpid(), thread.get_ident(), calendar.timegm(time.gmtime()))


def parse_os_credential_v2(os_credential_path):
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


def parse_os_credential_v3(os_credential_path):
    auth_url = None
    username = None
    password = None
    project_name = None
    project_domain_name = None
    user_domain_name = None

    with open(os_credential_path, 'r') as stream:
        try:
            data = yaml.load(stream)
            auth_url = data['clouds']['os']['auth']['auth_url']
            username = data['clouds']['os']['auth']['username']
            password = data['clouds']['os']['auth']['password']
            project_name = data['clouds']['os']['auth']['project_name']
            project_domain_name = data['clouds']['os']['auth']['project_domain_name']
            user_domain_name = data['clouds']['os']['auth']['user_domain_name']
        except yaml.YAMLError:
            LOGGER.critical('failed to parse os credential')

    return auth_url, username, password, project_name, project_domain_name, user_domain_name

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
