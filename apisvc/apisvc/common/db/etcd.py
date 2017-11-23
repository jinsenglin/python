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


def put_credential(account, credential_k8s, credential_os):
    _client.put('/apisvc/accounts/{0}'.format(account), 'ok')
    _client.put('/apisvc/accounts/{0}/k8s'.format(account), credential_k8s)
    _client.put('/apisvc/accounts/{0}/os'.format(account), credential_os)
