from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
import tenants
import users
import nodes


@ROUTE('/v1/admin/healthz')
@timeit
def v1_admin_healthz():
    return 'ok'
