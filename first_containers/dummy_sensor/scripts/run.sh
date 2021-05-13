#!/bin/bash
# sudo docker run --rm --name dummy-sensor-inst -v$PWD/app:/app -p8080:8080 cratustech/dummy-sensor:latest
sudo docker run --rm --name dummy-sensor-inst cratustech/dummy-sensor:latest
