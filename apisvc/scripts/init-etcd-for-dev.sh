#!/bin/bash

set -e

export ETCDCTL_API=3

cat ../samples/ca.key | etcdctl put /apisvc/ca/key
cat ../samples/ca.crt | etcdctl put /apisvc/ca/crt

cat ../samples/controller.k8s.yaml | etcdctl put /apisvc/controllers/k8s
cat ../samples/controller.os.yaml | etcdctl put /apisvc/controllers/os

etcdctl put /apisvc/nodes/comp1 ok
etcdctl put /apisvc/nodes/comp2 ok

etcdctl put /apisvc/accounts/0000-0000-0000-0000 ok
cat ../samples/0000-0000-0000-0000.k8s.yaml | etcdctl put /apisvc/accounts/0000-0000-0000-0000/k8s
cat ../samples/0000-0000-0000-0000.os.yaml | etcdctl put /apisvc/accounts/0000-0000-0000-0000/os
