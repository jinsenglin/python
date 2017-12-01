#!/bin/bash

# package dependency
# - kubectl
# - jq

# sample usage
# bash $0 /tmp ptt.log ../../samples/0000-0000-0000-0000.k8s.yaml

# sample output
# []

set -e

# input
TMP=$1
PTTLOG=$2
KUBECONFIG=$3

# output
PTTLOG_PATH=$TMP/$PTTLOG

# TODO bug - this will cause exit code always 0
kubectl --kubeconfig=$KUBECONFIG get ns -o json | jq '.items'

# clean up
# n/a
