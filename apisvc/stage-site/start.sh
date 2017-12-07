#!/bin/bash

set -e

/bin/flask run -h 0.0.0.0 -p 5080 --no-reload --no-debugger --eager-loading --without-threads