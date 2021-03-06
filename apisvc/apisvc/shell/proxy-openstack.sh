#!/bin/bash

# package dependency
# - openstack
# - jq

# sample usage
# bash $0 /tmp http://127.0.0.1:35357/v3/ admin passw0rd admin default default -f json

set -x
set -e

# input
TMP=$1; shift
export OS_AUTH_URL=$1; shift
export OS_USERNAME=$1; shift
export OS_PASSWORD=$1; shift
export OS_TENANT_NAME=$1; shift
export OS_PROJECT_DOMAIN_NAME=$1; shift
export OS_USER_DOMAIN_NAME=$1; shift
export OS_IDENTITY_API_VERSION=3

# output
DATA=$TMP/data

exec 3>&1
exec 1>&2

# main
openstack --insecure $@ > $DATA
if [[ "$@" == *" -f json" ]]; then
    jq '.' $DATA >&3
else
    cat $DATA >&3
fi

# clean up
[ -f $DATA ] && rm $DATA
