# Others


## Install dependency

```
# PROJECT_HOME = .

cd $PROJECT_HOME

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Start local etcd (via docker)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash bring-up-local-etcd.sh
```

## Init local etcd

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash init-etcd-db-for-dev.sh
```

## Init cache

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash clear-fs-cache.sh
bash init-fs-cache-for-dev.sh
```

## Start local openstack keystone (via docker)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash bring-up-local-os-keystone.sh
```

## Start local kubernetes (via minikube)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash bring-up-local-k8s.sh
```

## Start development server (single thread)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/apisvc

python main_dev.py
```

## Start development server (single thread, watch)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/apisvc

export FLASK_DEBUG=1
python main_dev.py
```

## Start development server (two threads)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/apisvc

gunicorn --workers=2 -b 127.0.0.1:5080 main_dev:app
```

## Start development server (single thread, production, option1, recommended)

```
# PROJECT_HOME = .

cd $PROJECT_HOME

export APISVC_MODE=DEBUG # optional
python -m apisvc
```

## Start development server (single thread, production, option2)

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

## Start development server (single thread, production, option3)

```
# PROJECT_HOME = .

cd $PROJECT_HOME

python setup.py install
cd apisvc
python main.py
```

## Start development server (single thread, production, option4)

```
# PROJECT_HOME = .

cd $PROJECT_HOME

python setup.py install
cd apisvc
gunicorn --workers=1 -b 127.0.0.1:5080 main:app
```

## Start development server (single thread, production, option5)

```
# PROJECT_HOME = .

cd $PROJECT_HOME

gunicorn --workers=1 -b 127.0.0.1:5080 apisvc:app
```

## Start development server (single thread, production, option6)

```
# PROJECT_HOME = .

cd $PROJECT_HOME

python setup.py install
cd $ANY_DIRECTORY
gunicorn --workers=1 -b 127.0.0.1:5080 apisvc:app
```
