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
KUBECONFIG=$2

# output
DATA=$TMP/data

exec 3>&1
exec 1>&2

# main
kubectl --kubeconfig=$KUBECONFIG get ns -o json > $DATA
jq '.items' $DATA >&3

# clean up
[ -f $DATA ] && rm $DATA
