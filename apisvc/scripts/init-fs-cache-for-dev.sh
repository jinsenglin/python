#!/bin/bash

set -e

[ -d ../apisvc/cache/0000-0000-0000-0000/ ] || mkdir -p ../apisvc/cache/0000-0000-0000-0000
cp ../samples/0000-0000-0000-0000.k8s.yaml ../apisvc/cache/0000-0000-0000-0000/k8s.yaml
cp ../samples/0000-0000-0000-0000.os.yaml ../apisvc/cache/0000-0000-0000-0000/os.yaml
