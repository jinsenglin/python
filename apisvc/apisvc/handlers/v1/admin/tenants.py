import json
from apisvc.common.log import LOGGER


def v1_admin_tenants_post(manager, response, *args, **kwargs):
    """
        create namespace
        create account
    """

    manager.create_namespace()
    manager.create_account()

    # update response
    # TODO

    # return response
    return json.dumps(response), {'Content-Type': 'application/json'}
