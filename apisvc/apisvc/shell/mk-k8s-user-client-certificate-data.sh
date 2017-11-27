#!/bin/bash

# package dependency
# - openssl
# - base64

# sample usage
# bash $0 ../../samples/ca.crt ../../samples/ca.key user1 role1

set -e

# input
CA_CRT=$1
CA_KEY=$2
CN=$3
O=$4

# output
KEY=server.key
CSR=server.csr
CRT=server.crt
CRT_BASE64=server.crt.base64
KEY_BASE64=server.key.base64

openssl req -new -sha256 -keyout $KEY -out $CSR -days 3650 -newkey rsa:2048 -nodes -subj "/O=$O/CN=$CN"
openssl x509 -req -days 3650 -sha1 -CA $CA_CRT  -CAkey $CA_KEY -CAcreateserial -in $CSR -out $CRT

base64 $CRT > $CRT_BASE64
base64 $KEY > $KEY_BASE64
