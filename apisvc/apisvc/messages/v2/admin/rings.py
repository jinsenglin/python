class Rings(object):

    def __init__(self):
        self.input_for_get = {}
        self.output_for_get = {'result': []}

        self.input_for_post = {}
        self.output_for_post = {'result': {}}


def new_message():
    return Rings()
