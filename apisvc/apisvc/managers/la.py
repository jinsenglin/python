import subprocess
import json
from apisvc.common.log import LOGGER
from apisvc.common.shell import mk_ks8_user_client_certificate_data as x


class Manager(object):
    def __init__(self):
        pass

    def mk_ks8_user_client_certificate_data(self, username, group='system:masters'):
        x(username=username, group='system:masters')

    def demo(self):
        output = ''

        try:
            output = subprocess.check_output('ls -l ../ | cat', shell=True)
            output = subprocess.check_output(['ls', '-l', '../'], shell=False)
        except subprocess.CalledProcessError:
            # TODO
            pass

        print(output)