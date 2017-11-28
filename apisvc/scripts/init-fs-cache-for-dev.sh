#!/bin/bash

set -e

[ -d ../apisvc/cache/ca/ ] || mkdir -p ../apisvc/cache/ca
cp ../samples/ca.key ../apisvc/cache/ca/ca.key
cp ../samples/ca.crt ../apisvc/cache/ca/ca.crt

[ -d ../apisvc/cache/accounts/0000-0000-0000-0000/ ] || mkdir -p ../apisvc/cache/accounts/0000-0000-0000-0000
cp ../samples/0000-0000-0000-0000.k8s.yaml ../apisvc/cache/accounts/0000-0000-0000-0000/k8s.yaml
cp ../samples/0000-0000-0000-0000.os.yaml ../apisvc/cache/accounts/0000-0000-0000-0000/os.yaml
