#!/bin/bash

set -e

echo "$(date) | INFO | clearing ../apisvc/cache/ca "
rm -rf ../apisvc/cache/ca              # do not keep ca/

echo "$(date) | INFO | clearing ../apisvc/cache/rings/admin/* "
rm -rf ../apisvc/cache/rings/admin/*   # keep rings/admin/

echo "$(date) | INFO | clearing ../apisvc/cache/rings/tenant/* "
rm -rf ../apisvc/cache/rings/tenant/*  # keep rings/tenant/

echo "$(date) | INFO | clearing ../apisvc/cache/rings/user/* "
rm -rf ../apisvc/cache/rings/user/*    # keep rings/user/
