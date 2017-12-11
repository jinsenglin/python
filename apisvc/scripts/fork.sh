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

for d in apisvc docs scripts stage-site tests
do
    find $d -type f ! -path scripts/fork.sh -exec sed -i "s/apisvc/$BRAND/g" '{}' \;
    find $d -type f ! -path scripts/fork.sh -exec sed -i "s/APISVC/$CBRAND/g" '{}' \;
done

exit 1

# ==============================

FILE=../README.md
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../SOURCE.md
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../setup.py
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../MANIFEST.in
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=./bring-up-fresh-dev-env.sh
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=./clear-fs-cache.sh
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=./init-etcd-db-for-dev.sh
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=./init-fs-cache-for-dev.sh
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../stage-site/README.md
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../stage-site/Vagrantfile
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../stage-site/apisvc.service
sed -i "s/apisvc/$BRAND/g" $FILE
mv $FILE ../stage-site/$BRAND.service

# ==============================

FILE=../stage-site/sync-data.sh
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FILE=../apisvc/DEBUG
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FOLDER=../apisvc
find $FOLDER -type f -name "*.py" -exec sed -i "s/apisvc/$BRAND/g" {} \;
mv $FOLDER ../$BRAND
