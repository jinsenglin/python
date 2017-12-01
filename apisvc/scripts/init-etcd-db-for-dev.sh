#!/bin/bash

set -e

export ETCDCTL_API=3

echo -n "$(date) | INFO | put /apisvc/ca "
etcdctl put /apisvc/ca ok

echo -n "$(date) | INFO | put /apisvc/ca/key "
cat ../samples/ca.key | etcdctl put /apisvc/ca/key

echo -n "$(date) | INFO | put /apisvc/ca/crt "
cat ../samples/ca.crt | etcdctl put /apisvc/ca/crt

echo -n "$(date) | INFO | put /apisvc/controllers/k8s "
cat ../samples/controller.k8s.yaml | etcdctl put /apisvc/controllers/k8s

echo -n "$(date) | INFO | put /apisvc/controllers/os "
cat ../samples/controller.os.yaml | etcdctl put /apisvc/controllers/os

echo -n "$(date) | INFO | put /apisvc/controllers/comp1 "
etcdctl put /apisvc/nodes/comp1 ok

echo -n "$(date) | INFO | put /apisvc/controllers/comp2 "
etcdctl put /apisvc/nodes/comp2 ok

echo -n "$(date) | INFO | put /apisvc/rings/admin/0000-0000-0000-0000 "
etcdctl put /apisvc/rings/admin/0000-0000-0000-0000 ok

echo -n "$(date) | INFO | put /apisvc/rings/admin/0000-0000-0000-0000/k8s "
cat ../samples/0000-0000-0000-0000.k8s.yaml | etcdctl put /apisvc/rings/admin/0000-0000-0000-0000/k8s

echo -n "$(date) | INFO | put /apisvc/rings/admin/0000-0000-0000-0000/os "
cat ../samples/0000-0000-0000-0000.os.yaml | etcdctl put /apisvc/rings/admin/0000-0000-0000-0000/os
