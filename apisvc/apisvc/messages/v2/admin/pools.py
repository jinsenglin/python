class Pools(object):

    def __init__(self):
        self.input_for_get = {}
        self.output_for_get = {'result': 'get'}

        self.input_for_post = {}
        self.output_for_post = {'result': 'post'}

        self.input_for_put = {}
        self.output_for_put = {'result': 'put'}

        self.input_for_delete = {}
        self.output_for_delete = {'result': 'delete'}


def new_message():
    return Pools()
