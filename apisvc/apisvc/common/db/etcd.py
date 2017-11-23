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


def put_account(account):
    # TODO use transaction to put account and credentials
    _client.put('/apisvc/accounts/{0}'.format(account), 'ok')


def put_credential(account, target, credential):
    _client.put('/apisvc/accounts/{0}/{1}'.format(account, target), credential)
