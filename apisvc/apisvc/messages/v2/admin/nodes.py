class Nodes(object):

    def __init__(self):
        self.input_for_get = {'filter': 'all'}
        self.output_for_get = {'result': []}


def new_message():
    return Nodes()
