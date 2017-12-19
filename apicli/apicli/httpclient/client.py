import requests


def post(cmd, arg):
    payload = {'cmd': cmd, 'arg': arg}
    result = requests.post('http://localhost:5080/porxy', data=payload)
    print(result)
