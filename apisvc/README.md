# Runtime Versions

* python: 2.7.11
* others: see requirements.txt and bindep.txt

# External Components

* openstack: >= mitaka (identity v3)
* kubernetes: 1.8.0
* etcd: 3.0.17

# Sources

* src home: apisvc
* entrypoints:
  * `__main__.py`
  * `main.py`
  * `main_dev.py`
* chain of responsibility: see SOURCE.md

# Logs

* file: /tmp/apisvc.log
* default log level: WARNING (CHANGE it to DEBUG in development site)

# Setup Development Environment

```
# PROJECT_HOME = .
cd $PROJECT_HOME
pip install -r requirements.txt
pip install -r requirements-dev.txt
bindep
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

cd $PROJECT_HOME/scripts && bash init-etcd-for-dev.sh # optional
cd $PROJECT_HOME/scripts && bash init-fs-cache-for-dev.sh # optional
```

Start local kubernetes

```
minikube start --kubernetes-version=v1.8.2 --bootstrapper kubeadm --cpus 4 --memory 8192
```

Start interactive shell

```
cd $PROJECT_HOME
export APISVC_MODE=DEBUG # optional
python

>>> import apisvc
>>> # for example
>>> apisvc.common.shell.ls_all_k8s_namespaces('samples/0000-0000-0000-0000.k8s.yaml')
>>> apisvc.common.shell.ls_all_os_projects('samples/0000-0000-0000-0000.os.yaml')
>>> apisvc.common.shell.proxy_kubectl('samples/0000-0000-0000-0000.k8s.yaml', ['get', 'ns'])
>>> apisvc.common.shell.proxy_openstack('samples/0000-0000-0000-0000.os.yaml', ['project', 'list'])
```

Start development server (single thread)

```
cd $PROJECT_HOME/apisvc
python main_dev.py
``` 

Start development server (single thread, watch)

```
cd $PROJECT_HOME/apisvc
export FLASK_DEBUG=1
python main_dev.py
``` 

Start development server (two threads)

```
cd $PROJECT_HOME/apisvc
gunicorn --workers=2 -b 127.0.0.1:5000 main_dev:app
```

Start development server (single thread, production, option1, recommended)

```
cd $PROJECT_HOME
export APISVC_MODE=DEBUG # optional
python -m apisvc
```

Start development server (single thread, production, option2)

```
cd $PROJECT_HOME
python setup.py install
cd $ANY_DIRECTORY
python -m apisvc

# To uninstall
# EGG=$(grep show apisvc | grep Location | awk '{print $2}')
# [ -z $EGG ] || rm $EGG
```

Start development server (single thread, production, option3)

```
cd $PROJECT_HOME
python setup.py install
cd apisvc
python main.py
```

Start development server (single thread, production, option4)

```
cd $PROJECT_HOME
python setup.py install
cd apisvc
gunicorn --workers=1 -b 127.0.0.1:5000 main:app
```

Start development server (single thread, production, option5)

```
cd $PROJECT_HOME
gunicorn --workers=1 -b 127.0.0.1:5000 apisvc:app
```

Start development server (single thread, production, option6)

```
cd $PROJECT_HOME
python setup.py install
cd $ANY_DIRECTORY
gunicorn --workers=1 -b 127.0.0.1:5000 apisvc:app
```

# PyCharm

1. Open PyCharm
2. Create New Project
3. Location: apisvc (NOTE not apisvc/apisvc)
4. Interpreter :: Add Local: apisvc/venv/bin/python2.7
5. Create :: Yes

# API References and Examples

* https://python-etcd3.readthedocs.io/en/latest/usage.html#api
* https://github.com/kubernetes-incubator/client-python/
* https://github.com/kubernetes-incubator/client-python/blob/master/kubernetes/README.md
* https://github.com/kubernetes-client/python-base/blob/b7a9f4a07eb39c41e7f813147a419ed0bfecbbd9/config/kube_config.py#L331
* https://developer.openstack.org/sdks/python/openstacksdk/users/index.html

# Addiontional Resources

* https://github.com/pallets/flask/tree/master/examples/patterns/largerapp
* https://medium.com/@timburks/openapi-and-grpc-side-by-side-b6afb08f75ed
* https://www.zopyx.com/andreas-jung/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
* https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
* http://flask.pocoo.org/docs/0.12/config/#builtin-configuration-values
* https://docs.python.org/2/library/logging.html#logging-levels
* http://flask.pocoo.org/docs/0.12/errorhandling/#logging-to-a-file
* http://trytofix.github.io/2016/05/05/Flask%E4%B8%AD%E4%BD%BF%E7%94%A8%E8%A3%85%E9%A5%B0%E5%99%A8%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98AssertionError-View-function-mapping-is-overwriting-an-existing-endpoint-function/
* http://ot-note.logdown.com/posts/67571/-decorator-with-without-arguments-in-function-class-form
* https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
* http://flask.pocoo.org/docs/dev/logging/#basic-configuration
* http://flask.pocoo.org/docs/dev/logging/#removing-the-default-handler
* http://flask.pocoo.org/docs/0.12/tutorial/setup/
* https://spacewander.github.io/explore-flask-zh/5-configuration.html
* http://blog.luisrei.com/articles/flaskrest.html
* http://codingpy.com/article/customizing-the-flask-response-class/
* https://docs.python.org/2/library/multiprocessing.html#synchronization-between-processes
* http://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Lock_Objects_Acquire_Release.php
* https://pyformat.info/
* https://pypi.python.org/pypi/fasteners
* https://redis.io/topics/distlock
* https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html
* http://www.infoq.com/cn/articles/how-to-implement-active-high-availability
* https://github.com/coreos/etcd/blob/master/Documentation/demo.md#distributed-locks
* flask-swagger vs. flasgger vs. flask-restful-swagger-2 vs. flask-restplus
* https://blog.aweimeow.tw/2016/09/09/python-subprocess-%E5%90%84%E5%87%BD%E5%BC%8F%E7%9A%84%E4%BD%BF%E7%94%A8%E6%99%82%E6%A9%9F/
