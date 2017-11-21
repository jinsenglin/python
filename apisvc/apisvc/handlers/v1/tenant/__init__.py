from apisvc import app


def quota(manager, *args, **kwargs):
    app.logger.debug('manager = {0}'.format(manager))
    return 'GET /v1/tenant/quota'
