import requests


def post(cmd, arg):
    headers = {'X-PERSONATE': 'admin 0000-0000-0000-0000'}
    payload = {'cmd': cmd, 'arg': arg}
    result = requests.post('http://localhost:5080/proxy', headers=headers, json=payload)
    print(result)
    print(result.json())
    print(result.json()['result'])
