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
vagrant up --provision-with poweron, upgrade

# access
curl http://192.168.33.10:5080/v2/admin/healthz

# runt tests
export APISVC_UT_ENDPOINT=192.168.33.10:5080
bash ../scripts/unit-test-via-curl.sh
```

# Docker container

```
bash sync-data.sh
docker build --rm -t local/apisvc .
docker run --privileged -dti -p 80:80 --name apisvc local/apisvc
docker run --privileged -dti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 80:80 --name apisvc local/apisvc

```
