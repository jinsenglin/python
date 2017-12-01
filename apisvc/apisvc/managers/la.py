import subprocess
import json
from apisvc.common.log import LOGGER
from apisvc.common import shell


class Manager(object):
    def __init__(self):
        pass

    def new_k8s_user_cert(self, username, group='system:masters'):
        """
            return a dict object
        """
        return shell.new_k8s_user_cert(username=username, group=group)

    def ls_all_os_projects(self, os_credential):
        """
            return a list object
        """
        return shell.ls_all_os_projects(os_credential=os_credential)

    def demo(self):
        output = ''

        try:
            output = subprocess.check_output('ls -l ../ | cat', shell=True)
            output = subprocess.check_output(['ls', '-l', '../'], shell=False)
        except subprocess.CalledProcessError:
            # TODO
            pass

        print(output)