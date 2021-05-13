#!/bin/bash
sudo docker run --rm --name flask-hub-inst -v$PWD/app:/app -p5000:5000 gibsoncratus/flask-hub-public:latest
