import re
from functools import wraps
from flask import request, abort
from apisvc.managers.gm import Manager
from apisvc.common import util
from apisvc.common.log import LOGGER
from apisvc.common.cache import fs as fs_cache


def _check_ring_existed(role, account):
    """
        return True if the specified ring exists in the local cache store
        return True if the specified ring exists in the remote persistent store
        return False if all checks are not passed
    """

    ring_key = fs_cache.get_ring_key(role=role, account=account)

    if ring_key is not None:
        LOGGER.debug('ring for role {0} account {1} found'.format(role, account))
        return True
    else:
        LOGGER.debug('ring for role {0} account {1} not found'.format(role, account))
        return False


PERSONATE_ADMIN = 'admin'
PERSONATE_TENANT = 'tenant'
PERSONATE_USER = 'user'


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
                    if _check_ring_existed(role=role, account=account):
                        kwargs['apisvc_res_manager'] = Manager(role=role, account=account)
                        result = fn(*args, **kwargs)
                        return result
                    else:
                        LOGGER.warn('aborting bad request due to no or wrong account present')
                        abort(400)
                else:
                    LOGGER.warn('aborting bad request due to no or wrong role present')
                    abort(400)
            else:
                LOGGER.warn('aborting bad request due to no X-PERSONATE header present')
                abort(400)
        return wrapper
    return need_personate_header_decorator


def check_body_against_in_message(in_message):
    """
        return HTTP status code 400 if body message format is wrong
        expand **kwargs by injecting an object 'apisvc_in_message' if all checks are passed
    """

    def check_body_against_in_message_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            LOGGER.debug('checking body content ... ')

            body_content = None
            try:
                body_content = request.get_json()
            except Exception as e:
                LOGGER.warn('aborting bad request due to invalid json body content present')
                abort(400)

            if body_content is None:
                body_content = {}

            if all(k in body_content for k, v in in_message.iteritems() if v is None):
                LOGGER.debug('checked body content ... ')
                in_message.update(body_content)
                kwargs['apisvc_in_message'] = in_message
                result = fn(*args, **kwargs)
                return result
            else:
                LOGGER.warn('aborting bad request due to wrong body content present')
                abort(400)

        return wrapper

    return check_body_against_in_message_decorator
