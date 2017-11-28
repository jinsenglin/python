import etcd3
from apisvc.common.config import CONFIG


_host = host = CONFIG['APISVC_DB_HOST']
_client = etcd3.client(host=_host)


def get_ca():
    value, key = _client.get('/apisvc/ca'.format())
    return value, key


def get_ca_pem(target):
    value, key = _client.get('/apisvc/ca/{0}'.format(target))
    return value, key


def get_account(account):
    value, key = _client.get('/apisvc/accounts/{0}'.format(account))
    return value, key


def get_credential(account, target):
    value, key = _client.get('/apisvc/accounts/{0}/{1}'.format(account, target))
    return value, key


def put_account_and_credentials(account, credential_k8s, credential_os):
    # TODO use transaction to put account and credentials
    _client.put('/apisvc/accounts/{0}'.format(account), 'ok')
    _client.put('/apisvc/accounts/{0}/{1}'.format(account, 'k8s'), credential_k8s)
    _client.put('/apisvc/accounts/{0}/{1}'.format(account, 'os'), credential_os)
