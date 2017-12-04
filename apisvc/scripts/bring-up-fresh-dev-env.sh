#!/bin/bash

# This helper script does not do the following:
#
# 1. clone source code
# 2. install packages
# 3. switch to python virtualenv
#
# which means you need do these manually in advance

set -e

if [ $# -eq 0 ]; then
    MODE=PART
else
    MODE=$1 # PART or FULL
fi

function clean_up {
    echo -n "$(date) | INFO | shutting down etcd db "
    docker stop etcd
    
    echo -n "$(date) | INFO | shutting down openstack keystone "
    docker stop os-keystone

    if [ $MODE == FULL ]; then
        echo "$(date) | INFO | shutting down minikube"
        minikube delete
    fi

    echo "$(date) | INFO | cleaned"
    exit
}
trap clean_up SIGINT SIGTERM

# =========================================================================================

echo "$(date) | INFO | clearing file-system cache"
bash clear-fs-cache.sh

# =========================================================================================

echo "$(date) | INFO | clearing lock files and log files and tmp files"
[ -f /tmp/apisvc-debug.log ] && rm  /tmp/apisvc-debug.log
[ -f /tmp/apisvc.lock ] && rm  /tmp/apisvc.lock
for tmp in $(find /tmp/ -type d -name "apisvc-*"); do rm -rf $tmp; done

# =========================================================================================

echo -n "$(date) | INFO | bringing up etcd db v3.0.17 "
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

# =========================================================================================

echo -n "$(date) | INFO | bringing up openstack keystone v9.1.0 (identity v3) "

docker run --rm -d -p 5000:5000 -p 35357:35357 --name os-keystone -e HOSTNAME=127.0.0.1 stephenhsu/keystone:9.1.0

# =========================================================================================

if [ $MODE == FULL ]; then
    echo "$(date) | INFO | bringing up minikube (kubernetes v1.8.0)"
    minikube start --kubernetes-version=v1.8.0 --bootstrapper kubeadm --cpus 2 --memory 4096
fi

# =========================================================================================

echo "$(date) | INFO | loading etcd server with initial data"
sleep 3
bash init-etcd-db-for-dev.sh

# =========================================================================================

echo "$(date) | INFO | bringing up http server"
export APISVC_MODE=DEBUG
cd ../ && gunicorn --workers=10 -b 127.0.0.1:5000 apisvc:app

# =========================================================================================
