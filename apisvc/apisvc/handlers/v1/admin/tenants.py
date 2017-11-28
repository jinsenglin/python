import json
from flask import request as flask_request
from apisvc.common.log import LOGGER


def v1_admin_tenants_post(manager, request, response, *args, **kwargs):
    """
        create namespace
        create account
    """

    manager.create_namespace()

    # update request
    # TODO check body
    body = flask_request.get_json()
    request.update(body)

    # update response
    # TODO

    # return response
    return json.dumps(response), {'Content-Type': 'application/json'}
