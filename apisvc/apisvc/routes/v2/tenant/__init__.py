import json
from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access


@ROUTE('/v2/tenant/healthz')
@timeit
@audit_anonymous_access
def v2_tenant_healthz():
    return 'ok', {'Content-Type': 'text/plain'}


@ROUTE('/v2/tenant/apis')
@timeit
@audit_anonymous_access
def v2_tenant_apis():
    return json.dumps({'status': 200,
                       'data': [{'method': 'GET', 'path': '/v2/tenant/healthz'},
                                {'method': 'GET', 'path': '/v2/tenant/apis'}
                                ]}), \
           {'Content-Type': 'application/json'}
