import requests


class Manager(object):
    def __init__(self):
        pass

    def demo(self):
        r = requests.get('https://api.github.com/events')
        print(r)