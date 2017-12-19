#!/bin/bash

set -e

echo -n "$(date) | INFO | restarting agent api mock "

docker restart agent-api-mock
