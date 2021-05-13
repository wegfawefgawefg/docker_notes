#!/bin/bash
sudo docker buildx build --platform linux/amd64,linux/arm64/v8 -t cratustech/dummy-sensor:latest --push .

#   arm only version
# sudo docker buildx build --platform linux/arm64/v8 -t cratustech/dummy-sensor:latest --push .
