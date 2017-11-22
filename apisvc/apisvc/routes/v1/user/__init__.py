from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
import vms
import pods


@ROUTE('/v1/user/healthz')
@timeit
def v1_user_healthz():
    return 'ok'
