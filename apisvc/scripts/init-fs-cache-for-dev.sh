#!/bin/bash

set -e

echo "$(date) | INFO | initing ../apisvc/cache/ca "
[ -d ../apisvc/cache/ca/ ] || mkdir -p ../apisvc/cache/ca
cp ../samples/ca.key ../apisvc/cache/ca/key.pem
cp ../samples/ca.crt ../apisvc/cache/ca/crt.pem

echo "$(date) | INFO | initing ../apisvc/cache/rings/admin/0000-0000-0000-0000 "
[ -d ../apisvc/cache/rings/admin/0000-0000-0000-0000/ ] || mkdir -p ../apisvc/cache/rings/admin/0000-0000-0000-0000
cp ../samples/0000-0000-0000-0000.k8s.yaml ../apisvc/cache/rings/admin/0000-0000-0000-0000/k8s.yaml
cp ../samples/0000-0000-0000-0000.os.yaml ../apisvc/cache/rings/admin/0000-0000-0000-0000/os.yaml
