#!/bin/bash

# This helper script does not do the following:
#
# 1. clone source code
# 2. install packages
# 3. switch to python virtualenv
#
# which means you need do these manually in advance

set -e

if [ $# -eq 0 ]; then
    MODE=PART
else
    MODE=$1 # PART or FULL
fi

function warning() {
    echo "$(date) | WARNING | unexpected exceptions. You need manually clean up the created fixtures."
}
trap warning ERR

function clean_up {
    echo -n "$(date) | INFO | shutting down etcd db "
    docker stop etcd
    
    echo -n "$(date) | INFO | shutting down openstack keystone "
    docker stop os-keystone

    if [ $MODE == FULL ]; then
        echo "$(date) | INFO | shutting down minikube"
        minikube delete
    fi

    echo "$(date) | INFO | cleaned"
    exit
}
trap clean_up SIGINT SIGTERM

# =========================================================================================

echo "$(date) | INFO | clearing file-system cache"
bash clear-fs-cache.sh

# =========================================================================================

echo "$(date) | INFO | clearing lock files and log files and tmp files"
[ -f /tmp/apisvc-debug.log ] && rm  /tmp/apisvc-debug.log
[ -f /tmp/apisvc.lock ] && rm  /tmp/apisvc.lock
for tmp in $(find /tmp/ -type d -name "apisvc-*"); do rm -rf $tmp; done

# =========================================================================================

bash bring-up-local-etcd.sh

# =========================================================================================

bash bring-up-local-os-keystone.sh

# =========================================================================================

if [ $MODE == FULL ]; then
    bash bring-up-local-os-keystone.sh
fi

# =========================================================================================

echo "$(date) | INFO | waiting etcd server ready"
sleep 3

echo "$(date) | INFO | loading etcd server with initial data"
bash init-etcd-db-for-dev.sh

# =========================================================================================

echo "$(date) | INFO | bringing up http server"
export APISVC_MODE=DEBUG
cd ../ && gunicorn --workers=10 -b 127.0.0.1:5080 apisvc:app

# =========================================================================================
