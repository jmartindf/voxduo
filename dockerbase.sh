#!/bin/bash

###
# Add more mounts for your projects after the git/gnupg/ssh ones
# e.g. -v ~/stuff/myproject:/project \

DOCKER=/usr/local/bin/finch

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
if $DOCKER ps | grep $name | awk '{ print $11 }'; then
	com=$($DOCKER rm -f $name)
	echo "Removed ${com}"
fi
$DOCKER run \
	--name $name \
	-p 8000:8000 \
	-v ~/Developer/blogs/voxduo:/project \
	${TTYARG} \
	git.desertflood.com/jmartindf/$img:latest \
	${RUNNER} -c "${CMD}"
