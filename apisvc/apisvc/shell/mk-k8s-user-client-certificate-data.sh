#!/bin/bash

# package dependency
# - openssl
# - base64
# - jq

# sample usage
# bash $0 /tmp ../../samples/ca.crt ../../samples/ca.key user1 role1
# bash $0 /tmp ../../samples/ca.crt ../../samples/ca.key cclin system:masters

set -e

# input
TMP=$1
CA_CRT=$2
CA_KEY=$3
CN=$4
O=$5

# output
KEY=$TMP/server.key
CSR=$TMP/server.csr
CRT=$TMP/server.crt
LOG=$TMP/$(basename $0).log

openssl req -new -sha256 -keyout $KEY -out $CSR -days 3650 -newkey rsa:2048 -nodes -subj "/O=$O/CN=$CN" > $LOG 2>&1
openssl x509 -req -days 3650 -sha1 -CA $CA_CRT  -CAkey $CA_KEY -CAcreateserial -in $CSR -out $CRT > $LOG 2>&1

jq -n "{
    \"crt\": \"$(base64 $CRT)\",
    \"key\": \"$(base64 $KEY)\"
}"

[ -f $KEY ] && rm $KEY
[ -f $CSR ] && rm $CSR
[ -f $CRT ] && rm $CRT
[ -f $LOG ] && rm $LOG
