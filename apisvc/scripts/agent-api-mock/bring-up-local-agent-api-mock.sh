#!/bin/bash

set -e

echo -n "$(date) | INFO | bringing up agent api mock "

docker run \
  --rm -d \
  -p 40080:40080 \
  -v $PWD:/opt \
  --name agent-api-mock \
  jimlintw/base:python-alpine python /opt/agent-api-mock.py
