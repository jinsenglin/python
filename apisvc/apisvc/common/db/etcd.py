import etcd3
from apisvc.common.config import CONFIG


_host = host = CONFIG['APISVC_DB_HOST']
_client = etcd3.client(host=_host)


def get_account(account):
    value, key = _client.get('/apisvc/accounts/{0}'.format(account))
    return value, key


def get_credential(account, target):
    value, key = _client.get('/apisvc/accounts/{0}/{1}'.format(account, target))
    return value, key
