import json
from apisvc.common.log import LOGGER


def apis(response, *args, **kwargs):
    # update response
    # TODO

    # return response
    return json.dumps(response), {'Content-Type': 'application/json'}
