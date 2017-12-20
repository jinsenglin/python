import requests


def put(endpoint, role, user, cmd, arg):
    url = '{0}/v2/admin/proxy/{1}'.format(endpoint, cmd)
    headers = {'X-PERSONATE': '{0} {1}'.format(role, user)}
    payload = {'arg': arg.split()}
    try:
        result = requests.put(url=url, headers=headers, json=payload)
        print(result.json()['result'])
    except requests.exceptions.ConnectionError:
        print('ERR_CONN_REFUSED')
