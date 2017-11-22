from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common import check
from apisvc.handlers.v1.tenant import quota as quota_handler
from apisvc.responses.v1.tenant import quota as quota_response
import vms
import pods


@ROUTE('/v1/tenant/healthz')
@timeit
def v1_tenant_healthz():
    return 'ok'


@ROUTE('/v1/tenant/quota')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
def v1_tenant_quota(*args, **kwargs):
    return quota_handler(manager=kwargs['apisvc_res_manager'], response=quota_response)
