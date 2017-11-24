from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access
from apisvc.handlers.v1.user import apis as apis_handler
from apisvc.responses.v1.user import apis as apis_response
import vms
import pods


@ROUTE('/v1/user/healthz')
@timeit
@audit_anonymous_access
def v1_user_healthz():
    return 'ok', {'Content-Type': 'text/plain'}


@ROUTE('/v1/user/apis')
@timeit
@audit_anonymous_access
def v1_user_apis():
    return apis_handler(response=apis_response)
