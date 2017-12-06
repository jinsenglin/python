#!/bin/bash

# package dependency
# - etcdctl

set -e

export ETCDCTL_API=3

APISVC_SAMPLES_DIR=${APISVC_SAMPLES_DIR:-"../samples"}

# ================== level 1 ======================

echo -n "$(date) | INFO | put /apisvc "
etcdctl put /apisvc ok

# ================== level 2 ======================

echo -n "$(date) | INFO | put /apisvc/controllers "
etcdctl put /apisvc/controllers ok

echo -n "$(date) | INFO | put /apisvc/nodes "
etcdctl put /apisvc/nodes ok

echo -n "$(date) | INFO | put /apisvc/rings "
etcdctl put /apisvc/rings ok

echo -n "$(date) | INFO | put /apisvc/ca "
etcdctl put /apisvc/ca ok

# ================== level 3 ======================

echo -n "$(date) | INFO | put /apisvc/controllers/k8s "
cat $APISVC_SAMPLES_DIR/controller.k8s.yaml | etcdctl put /apisvc/controllers/k8s

echo -n "$(date) | INFO | put /apisvc/controllers/os "
cat $APISVC_SAMPLES_DIR/controller.os.yaml | etcdctl put /apisvc/controllers/os

echo -n "$(date) | INFO | put /apisvc/nodes/compute "
etcdctl put /apisvc/nodes/compute ok

echo -n "$(date) | INFO | put /apisvc/rings/admin "
etcdctl put /apisvc/rings/admin ok

echo -n "$(date) | INFO | put /apisvc/rings/tenant "
etcdctl put /apisvc/rings/tenant ok

echo -n "$(date) | INFO | put /apisvc/rings/user "
etcdctl put /apisvc/rings/user ok

echo -n "$(date) | INFO | put /apisvc/ca/key "
cat $APISVC_SAMPLES_DIR/ca.key | etcdctl put /apisvc/ca/key

echo -n "$(date) | INFO | put /apisvc/ca/crt "
cat $APISVC_SAMPLES_DIR/ca.crt | etcdctl put /apisvc/ca/crt

# ================== level 4 ======================

echo -n "$(date) | INFO | put /apisvc/nodes/compute/comp1 "
cat $APISVC_SAMPLES_DIR/node.compute.comp1.json | etcdctl put /apisvc/nodes/compute/comp1

echo -n "$(date) | INFO | put /apisvc/nodes/compute/comp2 "
cat $APISVC_SAMPLES_DIR/node.compute.comp2.json | etcdctl put /apisvc/nodes/compute/comp2

echo -n "$(date) | INFO | put /apisvc/rings/admin/0000-0000-0000-0000 "
etcdctl put /apisvc/rings/admin/0000-0000-0000-0000 ok

# ================== level 5 ======================

echo -n "$(date) | INFO | put /apisvc/rings/admin/0000-0000-0000-0000/k8s "
cat $APISVC_SAMPLES_DIR/0000-0000-0000-0000.k8s.yaml | etcdctl put /apisvc/rings/admin/0000-0000-0000-0000/k8s

echo -n "$(date) | INFO | put /apisvc/rings/admin/0000-0000-0000-0000/os "
cat $APISVC_SAMPLES_DIR/0000-0000-0000-0000.os.yaml | etcdctl put /apisvc/rings/admin/0000-0000-0000-0000/os
