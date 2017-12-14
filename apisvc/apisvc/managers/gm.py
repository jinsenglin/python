import yaml
from apisvc.common import util
from apisvc.common.cache import fs as CACHE
from apisvc.managers import k8s
from apisvc.managers import os
from apisvc.managers import fbi
from apisvc.managers import cia
from apisvc.managers import ninja
from apisvc.common.log import LOGGER


class Manager(object):
    def __init__(self, role=None, account=None):
        # init rollback stacks
        self._rollback_needed = False
        self._rollback_stack = []
        self._rollback_kwargs_stack = []

        # init identity
        self._role = role
        self._account = account

        # init credential paths
        self._k8s_credential_path, self._os_credential_path = CACHE.get_credential_keys(role=role, account=account)

        # init ca file paths
        ca_key = CACHE.get_ca_key()

        if ca_key is None:
            self._ca_crt_path = None
            self._ca_key_path = None
            LOGGER.warning('ca not found. some actions can not work properly.')
        else:
            self._ca_crt_path, self._ca_key_path = CACHE.get_ca_pem_keys()

        # init managers
        self._k8s_mgr = k8s.Manager(credential_path=self._k8s_credential_path)
        self._os_mgr = os.Manager(credential_path=self._os_credential_path)
        self._fbi_mgr = fbi.Manager()
        self._cia_mgr = cia.Manager()
        self._ninja_mgr = ninja.Manager(k8s_credential_path=self._k8s_credential_path,
                                        os_credential_path=self._os_credential_path,
                                        ca_crt_path=self._ca_crt_path,
                                        ca_key_path=self._ca_key_path)

    def __str__(self):
        return '{0} {1}'.format(self._role, self._account)

    def _put_rollback(self, rollback, **rollback_kwargs):
        self._rollback_stack.append(rollback)
        self._rollback_kwargs_stack.append(rollback_kwargs)

    def _rollback(self):
        while len(self._rollback_stack) > 0:
            rollback = self._rollback_stack.pop()
            rollback_kwargs = self._rollback_kwargs_stack.pop()

            LOGGER.debug('issuing rollback {0}'.format(rollback))
            rollback(**rollback_kwargs)

    def rollback_if_needed(self):
        if self._rollback_needed:
            self._rollback()


    # ===================================== #
    #                                       #
    # node management                       #
    #                                       #
    # ===================================== #

    def get_nodes(self, node_filter):
        return self._fbi_mgr.get_nodes(node_filter=node_filter)

    def get_node(self, node_id, node_roles):
        return self._fbi_mgr.get_node(node_id=node_id, node_roles=node_roles)

    def update_node(self, node_id, node_role, node_action):
        if node_role == 'compute' and node_action in ['from_os_to_k8s', 'from_k8s_to_os']:
            node = self._fbi_mgr.get_node(node_id=node_id, node_roles=['compute'])
            node = yaml.load(node['result']['compute'])
            if node_action == 'from_os_to_k8s':
                return self._cia_mgr.switch_compute_node_from_os_to_k8s(node=node)
            else:
                # i.e. node_action == 'from_k8s_to_os':
                return self._cia_mgr.switch_compute_node_from_k8s_to_os(node=node)

        return {'result': {}}

    # ===================================== #
    #                                       #
    # pool management                       #
    #                                       #
    # ===================================== #

    def get_pools(self):
        return self._fbi_mgr.get_rings(ring_filter='tenant')

    def create_pool(self, tenant_id):
        # create k8s ns
        k8s_namespace = self._ninja_mgr.create_k8s_namespace(tenant_id=tenant_id)
        self._put_rollback(self._ninja_mgr.delete_k8s_namespace, tenant_id=tenant_id)

        # create os project
        os_project = self._ninja_mgr.create_os_project(tenant_id=tenant_id)
        self._put_rollback(self._ninja_mgr.delete_os_project, tenant_id=tenant_id)

        # create ring
        self.create_ring(tenant_id=tenant_id, account_id=tenant_id, ring_type='tenant')

        return {'result': {'k8s_namespace': k8s_namespace,
                           'os_project': os_project}}

    def get_pool(self, pool_id):
        # TODO delegate to k8s and os
        return {'result': {}}

    def update_pool(self, pool_id):
        # TODO delegate to k8s and os
        return {'result': {}}

    def delete_pool(self, pool_id):
        # TODO delegate to k8s and os
        return {'result': {}}

    # ===================================== #
    #                                       #
    # ring management                       #
    #                                       #
    # ===================================== #

    def get_rings(self, ring_filter):
        return self._fbi_mgr.get_rings(ring_filter=ring_filter)

    def create_ring(self, tenant_id, account_id, ring_type):
        # create os user
        os_user = self._ninja_mgr.create_os_user(tenant_id=tenant_id, account_id=account_id)
        self._put_rollback(self._ninja_mgr.delete_os_user, account_id=account_id)

        # create k8s user
        k8s_user = self._ninja_mgr.create_k8s_user(tenant_id=tenant_id, account_id=account_id)

        # create ring
        k8s_controller = self._fbi_mgr.get_controller('k8s')
        os_controller = self._fbi_mgr.get_controller('os')

        k8s_credential = util.native_k8s_user_object_to_ring_credential(k8s_controller=k8s_controller, k8s_user=k8s_user, k8s_ns=tenant_id)
        os_credential = util.native_os_user_object_to_ring_credential(os_controller=os_controller, os_user=os_user)

        ring = self._fbi_mgr.create_ring(ring_type=ring_type,
                                         account_id=account_id,
                                         k8s_credential=k8s_credential,
                                         os_credential=os_credential)
        self._put_rollback(self._fbi_mgr.delete_ring, ring_type=ring_type, account_id=account_id)

        return {'result': {'os_user': os_user, 'k8s_user': k8s_user, 'ring': ring}}

    def get_ring(self, ring_id):
        # TODO directly query etcd db
        return {'result': {}}

    def update_ring(self, ring_id):
        # TODO directly query etcd db
        return {'result': {}}

    def delete_ring(self, ring_id):
        # TODO delegate to k8s and os
        return {'result': {}}
