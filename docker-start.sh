#!/usr/bin/env bash

sudo docker stop raspy

result=$(sudo docker ps -a | grep raspy)
if [ ! -z "$result" ]
then
  echo "Docker already running."
  sudo docker rm raspy
fi

sudo docker run -it -p 9000:10000 --name raspy -v "$PWD/raspy":/raspy raspy ./init.sh
