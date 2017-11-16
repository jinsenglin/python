# Runtime Versions

* python: 2.7.11
* others: see requirements.txt

# External Components

* openstack: >= mitaka
* kubernetes: 1.8.2
* etcd: 3.0.17

# Sources

* src home: apisvc
* entrypoints:
  * main.py
  * main_dev.py
* chain of responsibility:
  * `__init__.py`
    * initiate object `app`
    * import package `routes`
  * `routes/__init__.py`
    * import package `routes.v1`
  * `routes/v1/__init__.py`
    * import module `routes.v1.admin`, which will trigger url registration
    * import module `routes.v1.tenant`, which will trigger url registration
    * import module `routes.v1.user`, which will trigger url registration
  * `routes/v1/admin.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/tenant.py`
    * import object `app`
    * invoke method `app.route()`
  * `routes/v1/user.py`
    * import object `app`
    * invoke method `app.route()`
  * `main.py`
    * import object `app`
    * invoke method `app.run()`

# Setup Development Environment

```
git clone ...
cd ...
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Start local etcd

```
export NODE1=127.0.0.1

REGISTRY=quay.io/coreos/etcd

docker run \
  --rm -d \
  -p 2379:2379 \
  -p 2380:2380 \
  --name etcd ${REGISTRY}:v3.0.17 \
  /usr/local/bin/etcd \
  --data-dir=/etcd-data --name node1 \
  --initial-advertise-peer-urls http://${NODE1}:2380 --listen-peer-urls http://0.0.0.0:2380 \
  --advertise-client-urls http://${NODE1}:2379 --listen-client-urls http://0.0.0.0:2379 \
  --initial-cluster node1=http://${NODE1}:2380
```

Start local kubernetes

```
minikube start --kubernetes-version=v1.8.2 --bootstrapper kubeadm --cpus 4 --memory 8192
```

Start development server (single thread)

```
cd apisvc
python main_dev.py
``` 

Start development server (two threads)

```
cd apisvc
gunicorn --workers=2 -b 127.0.0.1:5000 main_dev:app
```

Start development server (two threads, production)

```
python setup.py install
cd apisvc
gunicorn --workers=2 -b 127.0.0.1:5000 main:app
```

# API References and Examples

* https://python-etcd3.readthedocs.io/en/latest/usage.html#api
* https://github.com/kubernetes-incubator/client-python/
* https://github.com/kubernetes-incubator/client-python/blob/master/kubernetes/README.md
* https://github.com/kubernetes-client/python-base/blob/b7a9f4a07eb39c41e7f813147a419ed0bfecbbd9/config/kube_config.py#L331
* https://developer.openstack.org/sdks/python/openstacksdk/users/index.html

# Addiontional Resources

* https://github.com/pallets/flask/tree/master/examples/patterns/largerapp
* https://medium.com/@timburks/openapi-and-grpc-side-by-side-b6afb08f75ed
