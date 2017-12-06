#!/bin/bash

set -e

# (required)
cp apisvc.service data/
cp ../dist/apisvc-1.0.0.tar.gz data/
cp ../requirements.txt data/

# (optional)
cp ../scripts/bring-up-local-etcd.sh data/
cp ../scripts/bring-up-local-os-keystone.sh data/
