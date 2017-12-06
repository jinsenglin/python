#!/bin/bash

set -e

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
