#!/bin/bash

# This helper script does not do the following:
#
# 1. clone source code
# 2. install packages
# 3. switch to python virtualenv
#
# which means you need do these manually in advance

set -e

function clean_up {
  docker stop etcd

  echo cleaned
  exit
}
trap clean_up SIGINT SIGTERM

# =========================================================================================

echo "$(date) | INFO | clearing file-system cache"
bash clear-fs-cache.sh

# =========================================================================================

echo "$(date) | INFO | clearing lock files and log files"
[ -f /tmp/apisvc-debug.log ] && rm  /tmp/apisvc-debug.log
[ -f /tmp/apisvc.lock ] && rm  /tmp/apisvc.lock

# =========================================================================================

echo "$(date) | INFO | bringing up etcd server"
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

# TODO minikube

# =========================================================================================

echo "$(date) | INFO | loading etcd server with initial data"
sleep 3
bash init-etcd-for-dev.sh

# =========================================================================================

echo "$(date) | INFO | bringing up http server"
export APISVC_MODE=DEBUG
cd ../ && gunicorn --workers=10 -b 127.0.0.1:5000 apisvc:app

# =========================================================================================
