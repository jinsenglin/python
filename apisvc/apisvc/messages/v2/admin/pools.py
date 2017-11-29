class Pool(object):

    def __init__(self):
        self.input_for_get = {}
        self.output_for_get = {'status': 200, 'result': []}

        self.input_for_post = {}
        self.output_for_post = {'status': 200, 'result': 'post'}

        self.input_for_put = {}
        self.output_for_put = {'status': 200, 'result': 'put'}

        self.input_for_delete = {}
        self.output_for_delete = {'status': 200, 'result': 'delete'}


def new_message():
    return Pool()
