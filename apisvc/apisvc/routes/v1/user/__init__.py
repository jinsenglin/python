from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access
import vms
import pods


@ROUTE('/v1/user/healthz')
@timeit
@audit_anonymous_access
def v1_user_healthz():
    return 'ok'
