#!/bin/bash

# package dependency
# - kubectl
# - jq

# sample usage
# bash $0 /tmp ../../samples/0000-0000-0000-0000.k8s.yaml -o json

set -x
set -e

# input
TMP=$1
shift
KUBECONFIG=$1
shift

# output
DATA=$TMP/data

exec 3>&1
exec 1>&2

# main
kubectl --kubeconfig=$KUBECONFIG get ns $@ > $DATA
if [[ "$@" == *" -o json" ]]; then
    jq '.items' $DATA >&3
else
    cat $DATA >&3
fi

# clean up
[ -f $DATA ] && rm $DATA
