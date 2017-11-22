#!/bin/bash

set -e

export ETCDCTL_API=3
cat ../apisvc/cache/0000-0000-0000-0000.k8s.yaml | etcdctl put /apisvc/accounts/0000-0000-0000-0000/k8s
cat ../apisvc/cache/0000-0000-0000-0000.os.yaml | etcdctl put /apisvc/accounts/0000-0000-0000-0000/os
