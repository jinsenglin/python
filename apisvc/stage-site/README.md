# Vagrant machine

```
vagrant up
```

# Docker container

```
docker build --rm -t local/apisvc .
docker run --privileged -dti -p 80:80 --name apisvc local/apisvc
docker run --privileged -dti -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 80:80 --name apisvc local/apisvc

```
