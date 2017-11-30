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
    VER=v1
    CMD=healthz
elif [ $# -eq 1 ]; then
    VER=v1
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
    curl http://localhost:5000/$VER/admin/apis
    curl http://localhost:5000/$VER/tenant/apis
    curl http://localhost:5000/$VER/user/apis
}

function nodes() {
    curl http://localhost:5000/$VER/admin/nodes -H "X-PERSONATE: admin 0000-0000-0000-0000"
}

function pools() {
    curl http://localhost:5000/$VER/admin/pools -H "X-PERSONATE: admin 0000-0000-0000-0000"
}

function rings() {
    curl http://localhost:5000/$VER/admin/rings -H "X-PERSONATE: admin 0000-0000-0000-0000"
}

function tenant_quota() {
    curl http://localhost:5000/v1/tenant/quota -H "X-PERSONATE: TENANT 0000-0000-0000-0000"
}

function admin_tenants_post() {
    curl http://localhost:5000/v1/admin/tenants -X POST -H "X-PERSONATE: ADMIN 0000-0000-0000-0000"
}

function v2() {
    curl http://localhost:5000/v2/admin/tenants -H "X-PERSONATE: ADMIN 0000-0000-0000-0000"
    curl http://localhost:5000/v2/admin/tenants -H "X-PERSONATE: ADMIN 0000-0000-0000-0000" -X POST
    curl http://localhost:5000/v2/admin/tenants -H "X-PERSONATE: ADMIN 0000-0000-0000-0000" -X PUT
    curl http://localhost:5000/v2/admin/tenants -H "X-PERSONATE: ADMIN 0000-0000-0000-0000" -X DELETE
}

$CMD
