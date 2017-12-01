#!/bin/bash

# package dependency
# - openstack

# sample usage
# bash $0 /tmp http://192.168.228.31:5000/v2.0/ RegionOne jimlin jimlin jimlin

# sample output
# []

set -e

# input
TMP=$1
export OS_AUTH_URL=$2
export OS_REGION_NAME=$3
export OS_USERNAME=$4
export OS_PASSWORD=$5
export OS_TENANT_NAME=$6

# output
# n/a

openstack project list -f json

# clean up
# n/a
