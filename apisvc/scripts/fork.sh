#!/bin/bash

set -e

# Usage: $0 <new name> # e.g., XYZ

if [ $# -lt 2 ]; then
    echo "Usage: $0 <new name> <capital new name> # e.g., xyz XYZ"
    exit 1
fi
BRAND=$1
CBRAND=$2

# ==============================

for f in MANIFEST.in README.md setup.py
do
    sed -i "s/apisvc/$BRAND/g" $f
    sed -i "s/APISVC/$CBRAND/g" $f
done

for d in apisvc docs scripts stage-site tests
do
    find $d -type f ! -path scripts/fork.sh -exec sed -i "s/apisvc/$BRAND/g" '{}' \;
    find $d -type f ! -path scripts/fork.sh -exec sed -i "s/APISVC/$CBRAND/g" '{}' \;
done

mv stage-site/apisvc.service stage-site/$BRAND.service
mv apisvc $BRAND
