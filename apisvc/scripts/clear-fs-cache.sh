#!/bin/bash

set -e

rm -rf ../apisvc/cache/ca              # do not keep ca/
rm -rf ../apisvc/cache/rings/admin/*   # keep rings/admin/
rm -rf ../apisvc/cache/rings/tenant/*  # keep rings/tenant/
rm -rf ../apisvc/cache/rings/user/*    # keep rings/user/
