class Ring(object):

    def __init__(self):
        self.input_for_get = {}
        self.output_for_get = {'result': {}}

        self.input_for_put = {}
        self.output_for_put = {'result': {}}

        self.input_for_delete = {}
        self.output_for_delete = {'result': {}}


def new_message():
    return Ring()
