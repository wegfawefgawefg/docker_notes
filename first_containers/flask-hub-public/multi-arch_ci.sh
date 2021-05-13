#!/bin/bash

####    REQUIRES ARM64/v8 EMULATION     ####

sudo docker build -t gibsoncratus/flask-hub-public:latest-amd64 --build-arg ARCH=amd64 .
sudo docker build -t gibsoncratus/flask-hub-public:latest-arm64-v8 --build-arg ARCH=arm64v8 .
sudo docker push gibsoncratus/flask-hub-public:latest-amd64
sudo docker push gibsoncratus/flask-hub-public:latest-arm64-v8
sudo docker manifest create gibsoncratus/flask-hub-public:latest --amend gibsoncratus/flask-hub-public:latest-amd64 --amend gibsoncratus/flask-hub-public:latest-arm64-v8
