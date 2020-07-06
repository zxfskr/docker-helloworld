#!/bin/bash

#清理无名镜像
docker rmi  `docker images | grep none | awk '{print $3}'`

docker build -t fig/srs3:latest .