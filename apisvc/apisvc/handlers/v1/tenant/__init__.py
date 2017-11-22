import json
from apisvc.common.log import LOGGER


def quota(manager, response, *args, **kwargs):
    # use manager
    LOGGER.debug('manager = {0}'.format(manager))

    # update response
    response['message'] = 'GET /v1/tenant/quota'

    # return response
    return json.dumps(response)
