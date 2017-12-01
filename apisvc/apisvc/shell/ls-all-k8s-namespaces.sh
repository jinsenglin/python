#!/bin/bash

# package dependency
# - kubectl
# - jq

# sample usage
# bash $0 /tmp ../../samples/0000-0000-0000-0000.k8s.yaml

# sample output
# []

set -e

# input
TMP=$1
KUBECONFIG=$2

# output
# n/a

kubectl --kubeconfig=$KUBECONFIG get ns -o json | jq '.items'

# clean up
# n/a
