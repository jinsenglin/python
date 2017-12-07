import apisvc

from apisvc.common.db import etcd as DB

v, k = DB.get_ca()

print(v)
print(k)