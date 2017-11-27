import subprocess
import json
from apisvc.common.log import LOGGER


class Manager(object):
    def __init__(self):
        pass

    def mk_ks8_user_client_certificate_data(self, username, group='system:masters'):
        try:
            stdout = subprocess.check_output(['bash',
                                              'shell/mk-k8s-user-client-certificate-data.sh',
                                              '../../samples/ca.crt'
                                              '../../samples/ca.key',
                                              username,
                                              group], shell=False)
        except subprocess.CalledProcessError:
            LOGGER.error('failed to make k8s user client certificate data')

        data = json.loads(stdout)
        LOGGER.debug('key = {0}'.format(data['key']))
        LOGGER.debug('crt = {0}'.format(data['crt']))

    def demo(self):
        output = ''

        try:
            output = subprocess.check_output('ls -l ../ | cat', shell=True)
            output = subprocess.check_output(['ls', '-l', '../'], shell=False)
        except subprocess.CalledProcessError:
            # TODO
            pass

        print(output)