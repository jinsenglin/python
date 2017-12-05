#!/bin/bash

# package dependency
# - curl
# - jq

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
    echo "$(date) | INFO | GET /$VER/admin/healthz"
    curl http://localhost:5000/$VER/admin/healthz

    echo "$(date) | INFO | GET /$VER/tenant/healthz"
    curl http://localhost:5000/$VER/tenant/healthz

    echo "$(date) | INFO | GET /$VER/user/healthz"
    curl http://localhost:5000/$VER/user/healthz
}

function apis() {
    echo "$(date) | INFO | GET /$VER/admin/apis"
    curl http://localhost:5000/$VER/admin/apis | jq '.'

    echo "$(date) | INFO | GET /$VER/tenant/apis"
    curl http://localhost:5000/$VER/tenant/apis | jq '.'

    echo "$(date) | INFO | GET /$VER/user/apis"
    curl http://localhost:5000/$VER/user/apis | jq '.'
}

function nodes() {
    echo "$(date) | INFO | GET /$VER/admin/nodes | all nodes"
    curl http://localhost:5000/$VER/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'

    echo "$(date) | INFO | GET /$VER/admin/nodes | compute nodes"
    curl http://localhost:5000/$VER/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "compute"}' | jq '.'
}

function node() {
    echo "$(date) | INFO | GET /$VER/admin/node | compute node"
    curl http://localhost:5000/$VER/admin/nodes/comp1 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"roles": ["compute"]}' | jq '.'

    echo "$(date) | INFO | PUT /$VER/admin/node | switch compute node from os to k8s"
    curl http://localhost:5000/$VER/admin/nodes/comp1 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{"role": "compute", action: "from_os_to_k8s"}' | jq '.'

    echo "$(date) | INFO | PUT /$VER/admin/node | switch compute node from k8s to os"
    curl http://localhost:5000/$VER/admin/nodes/comp1 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{"role": "compute", action: "from_k8s_to_os"}' | jq '.'
}

function pools() {
    echo "$(date) | INFO | GET /$VER/admin/pools | all pools"
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'

    echo "$(date) | INFO | POST /$VER/admin/pools"
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "1111"}' | jq '.'
}

function pool() {
    curl http://localhost:5000/$VER/admin/pools/1111 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'
    curl http://localhost:5000/$VER/admin/pools/1111 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{}' | jq '.'
    curl http://localhost:5000/$VER/admin/pools/1111 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X DELETE | jq '.'
}

function rings() {
    echo "$(date) | INFO | GET /$VER/admin/rings | all rings"
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'

    echo "$(date) | INFO | GET /$VER/admin/rings | admin rings"
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "admin"}' | jq '.'

    echo "$(date) | INFO | GET /$VER/admin/rings | tenant rings"
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "tenant"}' | jq '.'

    echo "$(date) | INFO | GET /$VER/admin/rings | user rings"
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "user"}' | jq '.'

    echo "$(date) | INFO | POST /$VER/admin/rings"
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "1111", "account_id": "2222"}' | jq '.'
}

function ring() {
    curl http://localhost:5000/$VER/admin/rings/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'
    curl http://localhost:5000/$VER/admin/rings/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{}' | jq '.'
    curl http://localhost:5000/$VER/admin/rings/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X DELETE | jq '.'
}

function scenarios() {
    echo "$(date) | INFO | scenario of 2 tenants and each tenant has 2 users (shared pool model)"
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t1"}' | jq '.'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t1", "account_id": "u11"}' | jq '.'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t1", "account_id": "u12"}' | jq '.'
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t2"}' | jq '.'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t2", "account_id": "u21"}' | jq '.'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t2", "account_id": "u22"}' | jq '.'

    echo "$(date) | INFO | scenario of 2 tenants and each tenant only has 1 user (dedicated pool model)"
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "u3", "account_id": "u3"}' | jq '.'
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "u4", "account_id": "u4"}' | jq '.'
}

$CMD
