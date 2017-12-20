class Proxy(object):

    def __init__(self):
        self.input_for_put = {'arg': None}
        self.output_for_put = {'result': ''}


def new_message():
    return Proxy()
