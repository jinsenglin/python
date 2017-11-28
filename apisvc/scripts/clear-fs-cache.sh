#!/bin/bash

set -e

rm -rf ../apisvc/cache/ca           # do not keep ca/
rm -rf ../apisvc/cache/accounts/*   # keep accounts/
