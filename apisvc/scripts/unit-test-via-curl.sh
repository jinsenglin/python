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

set -e

APISVC_UT_VERSION=${APISVC_UT_VERSION:-"v2"}
APISVC_UT_ENDPOINT=${APISVC_UT_ENDPOINT:-"localhost:5080"}

if [ $# -eq 0 ]; then
    CMD=healthz
else
    CMD=$1
    shift
fi

function healthz() {
    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/healthz"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/healthz
    echo

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/tenant/healthz"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/tenant/healthz
    echo

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/user/healthz"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/user/healthz
    echo
}

function apis() {
    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/apis"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/apis | jq '.'

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/tenant/apis"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/tenant/apis | jq '.'

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/user/apis"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/user/apis | jq '.'
}

function nodes() {
    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/nodes | all nodes"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/nodes | compute nodes"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "compute"}' | jq '.'
}

function node() {
    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/node | compute node"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/nodes/comp1 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"roles": ["compute"]}' | jq '.'

    echo "$(date) | INFO | PUT /$APISVC_UT_VERSION/admin/node | switch compute node from os to k8s"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/nodes/comp1 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{"role": "compute", action: "from_os_to_k8s"}' | jq '.'

    echo "$(date) | INFO | PUT /$APISVC_UT_VERSION/admin/node | switch compute node from k8s to os"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/nodes/comp1 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{"role": "compute", action: "from_k8s_to_os"}' | jq '.'
}

function pools() {
    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/pools | all pools"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'

    echo "$(date) | INFO | POST /$APISVC_UT_VERSION/admin/pools"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "1111"}' | jq '.'
}

function pool() {
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools/1111 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools/1111 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools/1111 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X DELETE | jq '.'
}

function rings() {
    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/rings | all rings"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/rings | admin rings"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "admin"}' | jq '.'

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/rings | tenant rings"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "tenant"}' | jq '.'

    echo "$(date) | INFO | GET /$APISVC_UT_VERSION/admin/rings | user rings"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET -H "Content-Type: application/json" -d '{"filter": "user"}' | jq '.'

    echo "$(date) | INFO | POST /$APISVC_UT_VERSION/admin/rings"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "1111", "account_id": "2222"}' | jq '.'
}

function ring() {
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X GET | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X PUT -H "Content-Type: application/json" -d '{}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings/0 -H "X-PERSONATE: admin 0000-0000-0000-0000" -X DELETE | jq '.'
}

function scenarios() {
    echo "$(date) | INFO | scenario of 2 tenants and each tenant has 2 users (shared pool model)"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t1"}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t1", "account_id": "u11"}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t1", "account_id": "u12"}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t2"}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t2", "account_id": "u21"}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "t2", "account_id": "u22"}' | jq '.'

    echo "$(date) | INFO | scenario of 2 tenants and each tenant only has 1 user (dedicated pool model)"
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "u3", "account_id": "u3"}' | jq '.'
    curl -s http://$APISVC_UT_ENDPOINT/$APISVC_UT_VERSION/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000" -X POST -H "Content-Type: application/json" -d '{"tenant_id": "u4", "account_id": "u4"}' | jq '.'
}

$CMD
