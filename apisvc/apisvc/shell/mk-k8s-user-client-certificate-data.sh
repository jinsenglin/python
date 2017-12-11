#!/bin/bash

# package dependency
# - openssl
# - base64
# - jq

# sample usage
# bash $0 /tmp ../../samples/ca.crt ../../samples/ca.key user1 role1
# bash $0 /tmp ../../samples/ca.crt ../../samples/ca.key cclin system:masters

set -x
set -e

# input
TMP=$1
shift
CA_CRT=$1
shift
CA_KEY=$1
shift
CN=$1
shift
O=$1
shift

# output
DATA=$TMP/data
KEY=$TMP/server.key
CSR=$TMP/server.csr
CRT=$TMP/server.crt

exec 3>&1
exec 1>&2

# main
openssl req -new -sha256 -keyout $KEY -out $CSR -days 3650 -newkey rsa:2048 -nodes -subj "/O=$O/CN=$CN"
openssl x509 -req -days 3650 -sha1 -CA $CA_CRT  -CAkey $CA_KEY -CAcreateserial -in $CSR -out $CRT

jq -n "{
    \"crt\": \"$(base64 $CRT)\",
    \"key\": \"$(base64 $KEY)\"
}" >&3

# clean up
[ -f $DATA ] && rm $DATA
[ -f $KEY ] && rm $KEY
[ -f $CSR ] && rm $CSR
[ -f $CRT ] && rm $CRT
[ -f $LOG ] && rm $LOG
