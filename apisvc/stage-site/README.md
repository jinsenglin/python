# Target Environment

- Operating System: CentOS 7.2
- Python: 2.7.5

# Vagrant machine

```
# bootstrap
bash sync-data.sh
vagrant up

# restart
vagrant halt
vagrant up --provision-with poweron

# upgrade
vagrant halt
vagrant up --provision-with poweron,upgrade

# access
curl http://192.168.33.10:5080/v2/admin/healthz

# runt tests
export APISVC_UT_ENDPOINT=192.168.33.10:5080
bash ../scripts/unit-test-via-curl.sh
```

# Docker container

```
# build
bash sync-data.sh
docker build --rm -t local/apisvc .

# boostrap
docker run --rm --privileged -dti -p 5080:5080 --name apisvc local/apisvc

# runt tests
export APISVC_OS_HOST=172.17.0.1
bash ../scripts/bring-up-local-os-keystone.sh

export APISVC_DB_HOST=172.17.0.1
bash ../scripts/bring-up-local-os-keystone.sh

bash ../scripts/unit-test-via-curl.sh

# docker run --rm --privileged -dti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 80:80 -p 5080:5080 --name apisvc local/apisvc
```
