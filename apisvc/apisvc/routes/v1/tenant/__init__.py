from apisvc import app
from apisvc.common.profile import timeit
from apisvc.common import check
import vms
import pods


@app.route('/v1/tenant/healthz')
@timeit
def v1_tenant_healthz():
    return 'ok'


@app.route('/v1/tenant/quota')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
def v1_tenant_quota(*args, **kwargs):
    app.logger.debug('kwargs["apisvc_res_manager"] = {0}'.format(kwargs['apisvc_res_manager']))
    return 'GET /v1/tenant/quota'