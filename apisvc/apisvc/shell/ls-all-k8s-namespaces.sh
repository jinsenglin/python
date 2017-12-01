#!/bin/bash

# package dependency
# - kubectl
# - jq

# sample usage
# bash $0 /tmp ptt.log ../../samples/0000-0000-0000-0000.k8s.yaml

# sample output
# []

set -x
set -e

# input
TMP=$1
PTTLOG=$2
KUBECONFIG=$3

# output
PTTLOG_PATH=$TMP/$PTTLOG

exec 3>&1
exec 1>&2

# TODO bug - this will cause exit code always 0
kubectl --kubeconfig=$KUBECONFIG get ns -o json | jq '.items' >&3

# clean up
# n/a
