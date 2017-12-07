#!/bin/bash

set -e

echo "$(date) | INFO | bringing up minikube (kubernetes v1.8.0)"

minikube start --kubernetes-version=v1.8.0 --bootstrapper kubeadm --cpus 2 --memory 4096

