#!/bin/bash

# package dependency
# - openstack
# - jq

# sample usage
# bash $0 /tmp ptt.log http://192.168.228.31:5000/v2.0/ RegionOne jimlin jimlin jimlin

# sample output
# []

set -x
set -e

# input
TMP=$1
export OS_REGION_NAME=$2
export OS_AUTH_URL=$3
export OS_USERNAME=$4
export OS_PASSWORD=$5
export OS_TENANT_NAME=$6

# output
DATA=$TMP/data

exec 3>&1
exec 1>&2

# main
openstack project list -f json > $DATA
jq '.' $DATA >&3

# clean up
[ -f $DATA ] && rm $DATA
