#!/bin/bash

set -e

echo "$(date) | INFO | clearing ../apisvc/cache/ca "
[ -d ../apisvc/cache/ca ] && rm -rf ../apisvc/cache/ca              # do not keep ca/

echo "$(date) | INFO | clearing ../apisvc/cache/rings/admin/* "
find ../apisvc/cache/rings/admin -type d -maxdepth 1 -mindepth 1 -exec rm -rf {} \; # keep rings/admin/

echo "$(date) | INFO | clearing ../apisvc/cache/rings/tenant/* "
find ../apisvc/cache/rings/tenant -type d -maxdepth 1 -mindepth 1 -exec rm -rf {} \; # keep rings/tenant/

echo "$(date) | INFO | clearing ../apisvc/cache/rings/user/* "
find ../apisvc/cache/rings/user -type d -maxdepth 1 -mindepth 1 -exec rm -rf {} \; # keep rings/user/
