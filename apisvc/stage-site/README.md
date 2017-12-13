# Target Environment

- Operating System: CentOS 7.2
- Python: 2.7.5

# Vagrant machine

```
# build and bootstrap
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
bash ../scripts/bring-up-local-k8s.sh

export APISVC_UT_ENDPOINT=192.168.33.10:5080
bash ../scripts/unit-test-via-curl.sh
bash ../scripts/unit-test-via-curl.sh apis
bash ../scripts/unit-test-via-curl.sh nodes
bash ../scripts/unit-test-via-curl.sh pools
bash ../scripts/unit-test-via-curl.sh rings
```

# Docker container

```
# build
bash sync-data.sh
docker build --rm -t local/apisvc .

# boostrap
docker network create --subnet=172.18.0.0/16 mynet

export APISVC_DB_HOST=172.18.0.11
bash ../scripts/bring-up-local-etcd.sh

export APISVC_OS_HOST=172.18.0.12
bash ../scripts/bring-up-local-os-keystone.sh

docker run --rm --privileged -dti -p 5080:5080 --name apisvc --net mynet --link etcd:etcd --link os-keystone:os-keystone local/apisvc

# access
curl http://127.0.0.1:5080/v2/admin/healthz

# runt tests

# HACK init etcd and update systemd service unit
# - change samples/controller.os.yaml   : 127.0.0.1 -> os-keystone
# - change samples/0-0-0-0.os.yaml      : 127.0.0.1 -> os-keystone
#:: bash ../scripts/init-etcd-db-for-dev.sh
# - change stage-site/apisvc.service    : 127.0.0.1 -> etcd
#:: docker exec apisvc sed -i 's/127.0.0.1/etcd/' /usr/lib/systemd/system/apisvc.service
#:: docker exec apisvc systemctl daemon-reload
#:: docker exec apisvc systemctl restart apisvc

bash ../scripts/bring-up-local-k8s.sh

bash ../scripts/unit-test-via-curl.sh
bash ../scripts/unit-test-via-curl.sh apis
bash ../scripts/unit-test-via-curl.sh nodes
bash ../scripts/unit-test-via-curl.sh pools
bash ../scripts/unit-test-via-curl.sh rings
```
