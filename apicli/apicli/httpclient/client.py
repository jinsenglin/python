import requests


def put(cmd, arg):
    url = 'http://localhost:5080/v2/admin/proxy/{0}'.format(cmd)
    headers = {'X-PERSONATE': 'admin 0000-0000-0000-0000'}
    payload = {'arg': arg.split()}
    result = requests.put(url=url, headers=headers, json=payload)
    print(result.json()['result'])
