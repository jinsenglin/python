#!/bin/bash

set -e

echo -n "$(date) | INFO | bringing up agent api mock "

docker build -t local/agent-api-mock .
docker run \
  -d \
  -p 40080:40080 \
  -v $PWD:/opt \
  --name agent-api-mock \
  local/agent-api-mock python /opt/agent-api-mock.py
