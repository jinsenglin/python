# Test

## curl

```
# prerequisites
# start full fresh development server

# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash unit-test-via-curl.sh
```


## PyUnit

to test `apisvc.common.db.etcd` module

```
# prerequisites
# start local etcd
# init local etcd

# PROJECT_HOME = .

cd $PROJECT_HOME

python -m unittest discover tests/common/db/etcd "test_*.py"
```

to test `apisvc.common.db.etcd.get_ca` function

```
# prerequisites
# start local etcd
# init local etcd

# PROJECT_HOME = .

cd $PROJECT_HOME

python -m unittest tests.common.db.etcd.test_get_ca
```

to test `apisvc.managers.gm.create_pool` function

```
# prerequisites
# start local etcd
# start local openstack keystone
# start local kubernetes
# init local etcd
# init cache

# PROJECT_HOME = .

cd $PROJECT_HOME

python -m unittest tests.managers.gm.test_create_pool
```

to test `apisvc.managers.gm.create_ring` function

```
# prerequisites
# start local etcd
# start local openstack keystone
# start local kubernetes
# init local etcd
# init cache

# PROJECT_HOME = .

cd $PROJECT_HOME

python -m unittest tests.managers.gm.test_create_ring
```