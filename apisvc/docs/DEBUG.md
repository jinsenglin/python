# Debug

## Example 1 - debug shell

```
# prerequisites
# start local openstack keystone
# start local kubernetes

# PROJECT_HOME = .
cd $PROJECT_HOME
python # start interactive shell

>>> import apisvc
>>> apisvc.common.shell.ls_all_k8s_namespaces('samples/0000-0000-0000-0000.k8s.yaml')
>>> apisvc.common.shell.ls_all_os_projects('samples/0000-0000-0000-0000.os.yaml')
>>> apisvc.common.shell.proxy_kubectl('samples/0000-0000-0000-0000.k8s.yaml', ['get', 'ns'])
>>> apisvc.common.shell.proxy_openstack('samples/0000-0000-0000-0000.os.yaml', ['project', 'list'])
```

## Example 2 - debug gm

```
# prerequisites
# start local etcd
# start local openstack keystone
# start local kubernetes
# init local etcd
# init cache

# PROJECT_HOME = .
cd $PROJECT_HOME
python # start interactive shell

>>> import apisvc
>>> gm = apisvc.managers.gm.Manager(role='admin', account='0000-0000-0000-0000')
>>> gm.get_nodes(node_filter='all')
>>> gm.get_pools()
>>> gm.get_rings(ring_filter='all')
>>> gm.create_pool(tenant_id='t1')
```