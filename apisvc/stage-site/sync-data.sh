#!/bin/bash

set -e

[ -d data ] || mkdir data

# (required)
cp apisvc.service data/
cp ../dist/apisvc-1.0.0.tar.gz data/
cp ../requirements.txt data/
cp start.sh data/

# (optional)
cp ../scripts/bring-up-local-etcd.sh data/
cp ../scripts/bring-up-local-os-keystone.sh data/
cp ../scripts/init-etcd-db-for-dev.sh data/
cp -r ../samples data/
