#!/bin/bash

# package dependency
# - openstack
# - jq

# sample usage
# bash $0 /tmp http://192.168.228.31:5000/v2.0/ RegionOne jimlin jimlin jimlin

set -x
set -e

# input
TMP=$1
shift
export OS_REGION_NAME=$1
shift
export OS_AUTH_URL=$1
shift
export OS_USERNAME=$1
shift
export OS_PASSWORD=$1
shift
export OS_TENANT_NAME=$1
shift

unset OS_REGION_NAME
export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_IDENTITY_API_VERSION=3

# output
DATA=$TMP/data

exec 3>&1
exec 1>&2

# main
openstack $@ -f json > $DATA
jq '.' $DATA >&3

# clean up
[ -f $DATA ] && rm $DATA
