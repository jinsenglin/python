#!/bin/bash

# package dependency
# - openstack
# - jq

# sample usage
# bash $0 /tmp ptt.log http://192.168.228.31:5000/v2.0/ RegionOne jimlin jimlin jimlin

# sample output
# []

set -e

# input
TMP=$1
PTTLOG=$2
export OS_REGION_NAME=$3
export OS_AUTH_URL=$4
export OS_USERNAME=$5
export OS_PASSWORD=$6
export OS_TENANT_NAME=$7

# output
PTTLOG_PATH=$TMP/$PTTLOG

openstack project list -f json | jq '.'

# clean up
# n/a
