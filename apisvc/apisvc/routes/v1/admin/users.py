from apisvc import app
from apisvc.common.profile import timeit
from apisvc.common import check

@app.route('/v1/admin/users')
@timeit
@check.need_personate_header(check.PERSONATE_ADMIN)
def v1_admin_users(*args, **kwargs):
    return 'GET /v1/admin/users'
