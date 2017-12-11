#!/bin/bash

set -e

function print_section() {
    echo
    echo "[ $1 ]"
}

function check() {
    echo "$1 $(which $1)"
}

function print_foot() {
    echo
}

print_section init-etcd-db-for-dev.sh
check etcdctl

print_section unit-test-via-curl.sh
check jq
check curl

print_section bring-up-local-os-keystone.sh
check docker

print_section bring-up-local-k8s.sh
check minikube

print_section bring-up-local-etcd.sh
check docker

print_section bring-up-fresh-dev-env.sh
check docker
check minikube
check gunicorn

print_section proxy-openstack.sh
check openstack
check jq

print_section proxy-kubectl.sh
check kubectl
check jq

print_section mk-k8s-user-client-certificate-data.sh
check openssl
check base64
check jq

print_section requirements.txt
check pip
check gcc

print_section stage-site
check vagrant

print_foot
