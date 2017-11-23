import re
from functools import wraps
from flask import request, abort
from apisvc.managers.gm import Manager
from apisvc.common import util
from apisvc.common.log import LOGGER
from apisvc.common.db import etcd as etcd_db
from apisvc.common.cache import fs as fs_cache


def _check_account_existed_in_the_persistent_store(account):
    """
        if the specified account exists in the remote persistent store
        then cache it
        then return True
    """

    _, key = etcd_db.get_account(account)

    if key:
        credential_k8s, _ = etcd_db.get_credential(account, 'k8s')
        credential_os, _ = etcd_db.get_credential(account, 'os')
        fs_cache.put_account_and_credentials(account, credential_k8s, credential_os)
        LOGGER.debug('account {0} found in remote persistent store'.format(account))
        return True
    else:
        LOGGER.debug('account {0} not found in remote persistent store'.format(account))
        return False


def _check_account_existed(account):
    """
        return True if the specified account exists in the local cache store
        return True if the specified account exists in the remote persistent store
        return False if all checks are not passed
    """

    account_cached = fs_cache.get_account(account)

    if account_cached is not None:
        LOGGER.debug('account {0} found in local cache store'.format(account))
        return True
    else:
        LOGGER.debug('account {0} not found in local cache store'.format(account))
        return _check_account_existed_in_the_persistent_store(account)


PERSONATE_ADMIN = 'ADMIN'
PERSONATE_TENANT = 'TENANT'
PERSONATE_USER = 'USER'


def need_personate_header(role):
    """
        return HTTP status code 400 if there is no X-PERSONATE header in the request
        return HTTP status code 400 if there is no or wrong role specified in the value of X-PERSONATE header
        return HTTP status code 400 if the specified account does not exist in the system
        expand **kwargs by injecting an object 'apisvc_res_manager' if all checks are passed
    """

    def need_personate_header_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            LOGGER.debug('checking X-PERSONATE header ... ')

            if 'X-PERSONATE' in request.headers:
                personation = request.headers.get('X-PERSONATE')
                if re.match('{0} '.format(role), personation):
                    LOGGER.debug('personation = {0}'.format(personation))

                    _, account = util.personation_to_role_account(personation)
                    if _check_account_existed(account):
                        kwargs['apisvc_res_manager'] = Manager(role=role, account=account)
                        result = fn(*args, **kwargs)
                        return result
                    else:
                        LOGGER.debug('bad request, no or wrong account present')
                        abort(400)
                else:
                    LOGGER.debug('bad request, no or wrong role present')
                    abort(400)
            else:
                LOGGER.debug('bad request, no X-PERSONATE header present')
                abort(400)
        return wrapper
    return need_personate_header_decorator
