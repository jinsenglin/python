#!/bin/bash

set -e

export ETCDCTL_API=3

etcdctl put /apisvc/controllers/k8s ok
etcdctl put /apisvc/controllers/os ok

etcdctl put /apisvc/nodes/comp1 ok
etcdctl put /apisvc/nodes/comp2 ok

etcdctl put /apisvc/accounts/0000-0000-0000-0000 ok
cat ../samples/0000-0000-0000-0000.k8s.yaml | etcdctl put /apisvc/accounts/0000-0000-0000-0000/k8s
cat ../samples/0000-0000-0000-0000.os.yaml | etcdctl put /apisvc/accounts/0000-0000-0000-0000/os
