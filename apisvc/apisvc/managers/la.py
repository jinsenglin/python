import subprocess


class Manager(object):
    def __init__(self):
        pass

    def demo(self):
        output = ''

        try:
            output = subprocess.check_output(['ls', '-l', '../'])
        except subprocess.CalledProcessError:
            # TODO
            pass

        print(output)