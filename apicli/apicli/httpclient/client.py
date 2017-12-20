import requests
import simplejson


def put(endpoint, role, user, cmd, arg):
    url = '{0}/v2/admin/proxy/{1}'.format(endpoint, cmd)
    headers = {'X-PERSONATE': '{0} {1}'.format(role, user)}
    payload = {'arg': arg.split()}

    try:
        r = requests.put(url=url, headers=headers, json=payload, allow_redirects=True)
    except requests.exceptions.ConnectionError:
        print('ERR_CONN_REFUSED')
        return

    if r.status_code == requests.codes.ok:
        try:
            result = r.json()['result']
        except simplejson.errors.JSONDecodeError:
            print('ERR_BAD_RESPONSE :: JSONDecodeError')
            return
        except TypeError:
            print('ERR_BAD_RESPONSE :: TypeError')
            return
        except KeyError:
            print('ERR_BAD_RESPONSE :: KeyError')
            return

        print(result)
        return
    elif r.status_code == requests.codes.bad_request:
        print('ERR_BAD_REQUEST')
        return
    elif r.status_code == requests.codes.unauthorized:
        print('ERR_UNAUTHENTICATED')
        return
    elif r.status_code == requests.codes.forbidden:
        print('ERR_UNAUTHORIZED')
        return
    elif r.status_code == requests.codes.not_found:
        print('ERR_NOT_FOUND')
        return
    elif r.status_code == requests.codes.internal_server_error:
        print('ERR_INTERNAL_SERVER_ERROR')
        return
    else:
        print('ERR_OTHER_ERROR :: Status code = {0}'.format(r.status_code))
        return
