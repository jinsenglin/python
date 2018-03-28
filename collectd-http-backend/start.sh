#!/bin/bash

export MONASCA_API_URL=http://192.168.240.57:8070/v2.0/
export OS_USERNAME=mini-mon
export OS_PASSWORD=password
export OS_PROJECT_NAME=mini-mon
export OS_USER_DOMAIN_NAME=default
export OS_AUTH_URL=http://192.168.240.57:5000/v3/

python main.py
