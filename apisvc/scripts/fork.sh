#!/bin/bash

set -e

# Usage: $0 <new name>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <new name>"
    exit 1
fi
BRAND=$1

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

FILE=../apisvc/DEBUG
sed -i "s/apisvc/$BRAND/g" $FILE

# ==============================

FOLDER=../apisvc
find $FOLDER -type f -name "*.py" -exec sed -i "s/apisvc/$BRAND/g" {} \;
mv $FOLDER ../$BRAND
