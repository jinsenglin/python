# Source

* src home: apisvc
* entrypoints:
  * `__main__.py`
  * `main.py`
* chain of responsibility: see docs/SOURCE.md

# Dependency

see docs/DEPENDENCY.md

# Log

see docs/LOG.md

# Setup Development Environment

Install dependency

```
# PROJECT_HOME = .
cd $PROJECT_HOME
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Check dependency (via bindep.txt)

```
# PROJECT_HOME = .
cd $PROJECT_HOME
LANG=C bindep -f bindep.txt
```

Check dependency (via check-bindep.sh)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/scripts
bash check-bindep.sh
```

Start local etcd (via docker)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/scripts
bash bring-up-local-etcd.sh
```

Init local etcd

```
# PROJECT_HOME = .
cd $PROJECT_HOME/scripts
bash init-etcd-db-for-dev.sh
```

Init cache

```
# PROJECT_HOME = .
cd $PROJECT_HOME/scripts
bash clear-fs-cache.sh
bash init-fs-cache-for-dev.sh
```

Start local openstack keystone (via docker)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/scripts
bash bring-up-local-os-keystone.sh
```

Start local kubernetes (via minikube)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/scripts
bash bring-up-local-k8s.sh
```

Start development server (single thread)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/apisvc
python main_dev.py
``` 

Start development server (single thread, watch)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/apisvc
export FLASK_DEBUG=1
python main_dev.py
``` 

Start development server (two threads)

```
# PROJECT_HOME = .
cd $PROJECT_HOME/apisvc
gunicorn --workers=2 -b 127.0.0.1:5080 main_dev:app
```

Start development server (single thread, production, option1, recommended)

```
# PROJECT_HOME = .
cd $PROJECT_HOME
export APISVC_MODE=DEBUG # optional
python -m apisvc
```

Start development server (single thread, production, option2)

```
# PROJECT_HOME = .
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
# PROJECT_HOME = .
cd $PROJECT_HOME
python setup.py install
cd apisvc
python main.py
```

Start development server (single thread, production, option4)

```
# PROJECT_HOME = .
cd $PROJECT_HOME
python setup.py install
cd apisvc
gunicorn --workers=1 -b 127.0.0.1:5080 main:app
```

Start development server (single thread, production, option5)

```
# PROJECT_HOME = .
cd $PROJECT_HOME
gunicorn --workers=1 -b 127.0.0.1:5080 apisvc:app
```

Start development server (single thread, production, option6)

```
# PROJECT_HOME = .
cd $PROJECT_HOME
python setup.py install
cd $ANY_DIRECTORY
gunicorn --workers=1 -b 127.0.0.1:5080 apisvc:app
```

# Test

see docs/TEST.md

# Debug

see docs/DEBUG.md

# Build source distribution tarball

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts
bash clear-fs-cache.sh

cd $PROJECT_HOME
python setup.py sdist --formats=gztar
```

# Setup PyCharm

see docs/PyCharm.md


# Reference

see docs/REFERENCE.md
