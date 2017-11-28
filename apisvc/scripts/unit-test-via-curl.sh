#!/bin/bash

set -e

if [ -$# -eq 0 ]; then
    CMD=healthz
else
    CMD=$1
    shift
fi

function healthz() {
    curl http://localhost:5000/v1/admin/healthz
    curl http://localhost:5000/v1/tenant/healthz
    curl http://localhost:5000/v1/user/healthz
}

function apis() {
    curl http://localhost:5000/v1/admin/apis
    curl http://localhost:5000/v1/tenant/apis
    curl http://localhost:5000/v1/user/apis
}

function tenant_quota() {
    curl http://localhost:5000/v1/tenant/quota -H "X-PERSONATE: TENANT 0000-0000-0000-0000"
}

function admin_tenants_post() {
    curl http://localhost:5000/v1/admin/tenants -X POST -H "X-PERSONATE: ADMIN 0000-0000-0000-0000"
}

$CMD
