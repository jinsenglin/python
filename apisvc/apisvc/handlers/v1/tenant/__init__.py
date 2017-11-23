import json
from apisvc.common.log import LOGGER


def quota(manager, response, *args, **kwargs):
    # use manager
    # TODO

    # update response
    response['message'] = 'GET /v1/tenant/quota'

    # return response
    return json.dumps(response)
