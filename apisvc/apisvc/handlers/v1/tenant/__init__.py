import json
from apisvc.common.log import LOGGER


def apis(response, *args, **kwargs):
    # update response
    # TODO

    # return response
    return json.dumps(response)


def quota(manager, response, *args, **kwargs):
    # use manager
    # TODO

    # update response
    response['message'] = 'GET /v1/tenant/quota'

    # return response
    return json.dumps(response)
