import json
from apisvc.common.log import LOGGER


def v1_admin_tenants_post(manager, request, response, *args, **kwargs):
    """
        create namespace
        create account
    """

    manager.create_namespace()

    # update request
    # TODO
    #from flask import request
    #print(request.get_json())

    # update response
    # TODO

    # return response
    return json.dumps(response), {'Content-Type': 'application/json'}
