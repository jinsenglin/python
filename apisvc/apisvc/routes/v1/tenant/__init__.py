from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_access, audit_anonymous_access
from apisvc.common import check
from apisvc.handlers.v1.tenant import apis as apis_handler
from apisvc.responses.v1.tenant import apis as apis_response
from apisvc.handlers.v1.tenant import quota as quota_handler
from apisvc.responses.v1.tenant import quota as quota_response
import vms
import pods


@ROUTE('/v1/tenant/healthz')
@timeit
@audit_anonymous_access
def v1_tenant_healthz():
    return 'ok'


@ROUTE('/v1/tenant/apis')
@timeit
@audit_anonymous_access
def v1_tenant_apis():
    return apis_handler(response=apis_response)


@ROUTE('/v1/tenant/quota')
@timeit
@check.need_personate_header(check.PERSONATE_TENANT)
@audit_access
def v1_tenant_quota(*args, **kwargs):
    return quota_handler(manager=kwargs['apisvc_res_manager'], response=quota_response)
