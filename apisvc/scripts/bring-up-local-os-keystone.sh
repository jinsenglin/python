#!/bin/bash

set -e

echo -n "$(date) | INFO | bringing up openstack keystone v9.1.0 (identity v3) "

docker run --rm -d -p 5000:5000 -p 35357:35357 --name os-keystone -e HOSTNAME=127.0.0.1 stephenhsu/keystone:9.1.0
