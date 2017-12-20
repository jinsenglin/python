import json
from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access

@ROUTE('/v2/admin/healthz')
@timeit
@audit_anonymous_access
def v2_admin_healthz():
    return 'ok', {'Content-Type': 'text/plain'}


@ROUTE('/v2/admin/apis')
@timeit
@audit_anonymous_access
def v2_admin_apis():
    return json.dumps({'status': 200,
                       'data': [{'method': 'GET', 'path': '/v2/admin/healthz'},
                                {'method': 'GET', 'path': '/v2/admin/apis'},
                                {'method': 'GET', 'path': '/v2/admin/nodes'},
                                {'method': 'GET', 'path': '/v2/admin/nodes/compute'},
                                {'method': 'GET', 'path': '/v2/admin/nodes/:id'},
                                {'method': 'PUT', 'path': '/v2/admin/nodes/:id'},
                                {'method': 'GET', 'path': '/v2/admin/pools'},
                                {'method': 'POST', 'path': '/v2/admin/pools'},
                                {'method': 'GET', 'path': '/v2/admin/pools/:id'},
                                {'method': 'PUT', 'path': '/v2/admin/pools/:id'},
                                {'method': 'DELETE', 'path': '/v2/admin/pools/:id'},
                                {'method': 'GET', 'path': '/v2/admin/rings'},
                                {'method': 'POST', 'path': '/v2/admin/rings'},
                                {'method': 'GET', 'path': '/v2/admin/rings/:id'},
                                {'method': 'PUT', 'path': '/v2/admin/rings/:id'},
                                {'method': 'DELETE', 'path': '/v2/admin/rings/:id'}
                                ]}), \
           {'Content-Type': 'application/json'}
