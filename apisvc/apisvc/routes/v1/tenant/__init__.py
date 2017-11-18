from apisvc import app
from apisvc.common.profile import timeit
from apisvc.common import check

@app.route('/v1/tenant/healthz')
@timeit
def v1_tenant_healthz():
    return 'ok'

@app.route('/v1/tenant/quota')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
def v1_tenant_quota():
    return 'GET /v1/tenant/quota'

import vms
import pods
