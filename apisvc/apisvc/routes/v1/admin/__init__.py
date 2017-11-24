from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access
import tenants
import users
import nodes


@ROUTE('/v1/admin/healthz')
@timeit
@audit_anonymous_access
def v1_admin_healthz():
    return 'ok'
