#!/bin/bash

set -e

[ -d /var/cache/apisvc ] || cp -r /usr/lib/python2.7/site-packages/apisvc/cache /var/cache/apisvc
[ -d /var/lock/apisvc ] || mkdir -p /var/lock/apisvc
[ -d /var/log/apisvc ] || mkdir -p /var/log/apisvc
[ -d /tmp/apisvc ] || mkdir -p /tmp/apisvc

/bin/flask run -h 0.0.0.0 -p 5080 --no-reload --no-debugger --eager-loading --without-threads
