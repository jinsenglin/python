#!/bin/bash

# Usage
#
# $0
#
# $0 healthz
#
# $0 v1 healthz
# 

set -e

if [ $# -eq 0 ]; then
    VER=v2
    CMD=healthz
elif [ $# -eq 1 ]; then
    VER=v2
    CMD=$1
    shift
else
    VER=$1
    shift
    CMD=$1
    shift
fi

function healthz() {
    curl http://localhost:5000/$VER/admin/healthz
    curl http://localhost:5000/$VER/tenant/healthz
    curl http://localhost:5000/$VER/user/healthz
}

function apis() {
    curl http://localhost:5000/$VER/admin/apis | jq '.'
    curl http://localhost:5000/$VER/tenant/apis | jq '.'
    curl http://localhost:5000/$VER/user/apis | jq '.'
}

function nodes() {
    curl http://localhost:5000/$VER/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET
    curl http://localhost:5000/$VER/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "compute"}'
}

function node() {
    curl http://localhost:5000/$VER/admin/nodes/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET
    curl http://localhost:5000/$VER/admin/nodes/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{}'
}

function pools() {
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -d '{}'
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -d '{}'
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X DELETE -d '{}'
}

function rings() {
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -d '{}'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -d '{}'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X DELETE -d '{}'
}

$CMD
