#!/bin/bash

###
# Add more mounts for your projects after the git/gnupg/ssh ones
# e.g. -v ~/stuff/myproject:/project \

if [[ -t 0 ]] && [[ -t 1 ]]; then
	# Not running in a batch / scheduled task
	TTYARG="-ti"
else
	# Is running in a batch / scheduled task
	TTYARG=""
fi

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
${TTYARG} \
jmartindf/$img:latest \
${RUNNER} -c "${CMD}"
