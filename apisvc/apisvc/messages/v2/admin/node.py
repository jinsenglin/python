class Node(object):

    def __init__(self):
        self.input_for_get = {}
        self.output_for_get = {'result': {}}

        self.input_for_put = {}
        self.output_for_put = {'result': {}}


def new_message():
    return Node()
