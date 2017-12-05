# Target Environment

- Operating System: CentOS 7.2
- Python: 2.7.5

# Vagrant machine

```
bash sync-data.sh
vagrant up
```

# Docker container

```
bash sync-data.sh
docker build --rm -t local/apisvc .
docker run --privileged -dti -p 80:80 --name apisvc local/apisvc
docker run --privileged -dti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 80:80 --name apisvc local/apisvc

```