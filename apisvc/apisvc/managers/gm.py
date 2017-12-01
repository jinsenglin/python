from apisvc.common.cache import fs as fs_cache
from apisvc.managers import k8s
from apisvc.managers import os
from apisvc.managers import cia
from apisvc.managers import la
from apisvc.common.log import LOGGER


class Manager(object):
    def __init__(self, role=None, account=None):
        # init identity
        self._role = role
        self._account = account

        # init credential paths
        self._k8s_credential_path, self._os_credential_path = fs_cache.get_credential_keys(role=role, account=account)

        # init managers
        self._k8s_mgr = k8s.Manager(credential_path=self._k8s_credential_path)
        self._os_mgr = os.Manager(credential_path=self._os_credential_path)
        self._cia_mgr = cia.Manager()
        self._la_mgr = la.Manager(k8s_credential_path=self._k8s_credential_path,
                                  os_credential_path=self._os_credential_path)

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account)

    # ===================================== #
    #                                       #
    # node management                       #
    #                                       #
    # ===================================== #

    def get_nodes(self, filter):
        # TODO directly query etcd db
        return {}

    def get_node(self, id):
        # TODO directly query etcd db
        return {}

    def update_node(self, id):
        # TODO delegate to cia
        return {}

    # ===================================== #
    #                                       #
    # pool management                       #
    #                                       #
    # ===================================== #

    def get_pools(self):
        # TODO directly query etcd db
        data = self._la_mgr.ls_all_os_projects()
        data = self._la_mgr.ls_all_k8s_namespaces()
        return {'result': data}

    def create_pool(self, tenant_id):
        """
            create pool
            create ring
        """

        # TODO delegate to k8s and os

        return {}

    def get_pool(self, id):
        # TODO delegate to k8s and os
        return {}

    def update_pool(self, id):
        # TODO delegate to k8s and os
        return {}

    def delete_pool(self, id):
        # TODO delegate to k8s and os
        return {}

    # ===================================== #
    #                                       #
    # ring management                       #
    #                                       #
    # ===================================== #

    def get_rings(self):
        # TODO directly query etcd db
        return {}

    def create_ring(self, tenant_id, account_id):
        """
            create ring
        """

        # TODO delegate to k8s and os

        return {}

    def get_ring(self, id):
        # TODO directly query etcd db
        return {}

    def update_ring(self, id):
        # TODO directly query etcd db
        return {}

    def delete_ring(self, id):
        # TODO delegate to k8s and os
        return {}

#    def create_namespace(self):
#        """
#            create namespace
#            create account
#            return True of False
#
#        """
#
#        LOGGER.debug('namespace created')
#
#        created = self.create_account()
#
#        if created:
#            LOGGER.debug('account created')
#            return True
#        else:
#            LOGGER.debug('account not created')
#
#        return False
#
#    def create_account(self):
#        """
#            create k8s account
#            create os account
#            return True or False
#        """
#
#        data = self._la_mgr.new_k8s_user_cert('cclin')
#
#        if data is not None:
#            LOGGER.debug('account created')
#            # TODO update db
#            # TODO update cache
#            # TODO update k8s
#            # TODO update os
#            return True
#        else:
#            LOGGER.debug('account not created')
#
#        return False
