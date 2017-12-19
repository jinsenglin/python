import json
from apisvc.common.route import ROUTE
from apisvc.common.profile import timeit
from apisvc.common.audit import audit_anonymous_access


@ROUTE('/proxy', methods=['POST'])
@timeit
@audit_anonymous_access
def proxy():
    from flask import request
    return json.dumps({'status': 200, 'data': request.get_json()}), \
           {'Content-Type': 'application/json'}
