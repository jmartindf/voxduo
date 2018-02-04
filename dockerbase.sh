#!/bin/bash

###
# Add more mounts for your projects after the git/gnupg/ssh ones
# e.g. -v ~/stuff/myproject:/project \

wd=$(pwd)
img=docker-pelican
name=pelican-voxduo
if docker ps | grep $name | awk '{ print $11 }'
    then
    com=$(docker rm -f $name)
    echo "Removed ${com}"
fi
docker run \
--name $name \
-p 8000:8000 \
-v ~/development/blogs/voxduo:/project \
-ti \
jmartindf/$img:latest \
${RUNNER} -c "${CMD}"
