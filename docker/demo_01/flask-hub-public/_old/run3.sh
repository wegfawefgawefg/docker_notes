#!/bin/bash

# deployment should be managed within a yaml
#   do not use this file...

START_PORT=5005
NUM_LAUNCH=3
END_PORT=$(( $START_PORT + $NUM_LAUNCH ))

for i in $(seq $START_PORT $END_PORT); do
    sudo docker run -v$PWD/app:/app -p"$i":"$i" gibsoncratus/flask-hub-public:latest
done