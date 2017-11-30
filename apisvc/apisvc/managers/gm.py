from apisvc.common.cache import fs as fs_cache
from apisvc.managers import k8s
from apisvc.managers import os
from apisvc.managers import cia
from apisvc.managers import la
from apisvc.common.log import LOGGER


class Manager(object):
    def __init__(self, role=None, account=None):
        self._role = role
        self._account = account

        credential_key_k8s, credential_key_os = fs_cache.get_credential_keys(role=role, account=account)
        self._k8s_mgr = k8s.Manager(credential_key=credential_key_k8s)
        self._os_mgr = os.Manager(credential_key=credential_key_os)
        self._cia_mgr = cia.Manager()
        self._la_mgr = la.Manager()

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account)

    def demo(self):
        self._k8s_mgr.demo()
        self._os_mgr.demo()
        self._cia_mgr.demo()
        self._la_mgr.demo()

    def create_pool(self, tenant_id):
        """
            create pool
            create ring
        """

        # TODO

        return {}

    def create_ring(self, tenant_id, account_id):
        """
            create ring
        """

        # TODO

        return {}

    def create_namespace(self):
        """
            create namespace
            create account
            return True of False

        """

        LOGGER.debug('namespace created')

        created = self.create_account()

        if created:
            LOGGER.debug('account created')
            return True
        else:
            LOGGER.debug('account not created')

        return False

    def create_account(self):
        """
            create k8s account
            create os account
            return True or False
        """

        data = self._la_mgr.new_k8s_user_cert('cclin')

        if data is not None:
            LOGGER.debug('account created')
            # TODO update db
            # TODO update cache
            # TODO update k8s
            # TODO update os
            return True
        else:
            LOGGER.debug('account not created')

        return False
