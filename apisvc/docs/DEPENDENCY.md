# Dependency

## External Systems

* etcd: 3.0.17
* openstack: keystone v9.1.0 identity v3
* kubernetes: 1.8.0

## Runtime Dependencies

* python: 2.7.x (my version: 2.7.11)
* others: see requirements.txt, requirements-dev.txt and bindep.txt

## Check dependency (via bindep.txt)

```
# PROJECT_HOME = .

cd $PROJECT_HOME

LANG=C bindep -f bindep.txt
```

## Check dependency (via check-bindep.sh)

```
# PROJECT_HOME = .

cd $PROJECT_HOME/scripts

bash check-bindep.sh
```