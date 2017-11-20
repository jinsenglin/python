class Manager(object):
    # TODO
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account);
