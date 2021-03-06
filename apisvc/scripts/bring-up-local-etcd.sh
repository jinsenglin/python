#!/bin/bash

set -e

APISVC_DB_HOST=${APISVC_DB_HOST:-127.0.0.1}

echo -n "$(date) | INFO | bringing up etcd db v3.0.17 "

REGISTRY=quay.io/coreos/etcd

if [ $APISVC_DB_HOST == "127.0.0.1" ]; then
docker run \
  --rm -d \
  -p 2379:2379 \
  -p 2380:2380 \
  --name etcd ${REGISTRY}:v3.0.17 \
  /usr/local/bin/etcd \
  --data-dir=/etcd-data --name node1 \
  --initial-advertise-peer-urls http://${APISVC_DB_HOST}:2380 --listen-peer-urls http://0.0.0.0:2380 \
  --advertise-client-urls http://${APISVC_DB_HOST}:2379 --listen-client-urls http://0.0.0.0:2379 \
  --initial-cluster node1=http://${APISVC_DB_HOST}:2380
else
docker run \
  --net mynet --ip $APISVC_DB_HOST \
  --rm -d \
  -p 2379:2379 \
  -p 2380:2380 \
  --name etcd ${REGISTRY}:v3.0.17 \
  /usr/local/bin/etcd \
  --data-dir=/etcd-data --name node1 \
  --initial-advertise-peer-urls http://${APISVC_DB_HOST}:2380 --listen-peer-urls http://0.0.0.0:2380 \
  --advertise-client-urls http://${APISVC_DB_HOST}:2379 --listen-client-urls http://0.0.0.0:2379 \
  --initial-cluster node1=http://${APISVC_DB_HOST}:2380
fi

echo "$(date) | DEBUG | APISVC_DB_HOST = $APISVC_DB_HOST"
