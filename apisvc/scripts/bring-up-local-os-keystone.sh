#!/bin/bash

set -e

APISVC_OS_HOST=${APISVC_OS_HOST:-127.0.0.1}

echo -n "$(date) | INFO | bringing up openstack keystone v9.1.0 (identity v3) "

if [ $APISVC_OS_HOST == "127.0.0.1" ]; then
    docker run --rm -d -p 5000:5000 -p 35357:35357 --name os-keystone -e HOSTNAME=$APISVC_OS_HOST stephenhsu/keystone:9.1.0
else
    docker run --rm -d -p 5000:5000 -p 35357:35357 --name os-keystone --net mynet --ip $APISVC_OS_HOST -e HOSTNAME=$APISVC_OS_HOST stephenhsu/keystone:9.1.0
fi

echo "$(date) | DEBUG | APISVC_OS_HOST= $APISVC_OS_HOST "
