from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access
from apisvc.handlers.v1.admin import apis as apis_handler
from apisvc.responses.v1.admin import apis as apis_response
import tenants
import users
import nodes


@ROUTE('/v1/admin/healthz')
@timeit
@audit_anonymous_access
def v1_admin_healthz():
    return 'ok', {'Content-Type': 'text/plain'}


@ROUTE('/v1/admin/apis')
@timeit
@audit_anonymous_access
def v1_admin_apis():
    return apis_handler(response=apis_response)
