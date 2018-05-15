PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
PRDCONF=$(BASEDIR)/prdconf.py

SSH_HOST=mark.desertflood.com
SSH_PORT=22
SSH_USER=blogs
SSH_TARGET_DIR=/home/blogs/public/voxduo-dev/www
PRD_SSH_TARGET_DIR=/home/blogs/public/voxduo/www

RSYNC_TARGET_DIR=/home/blogs/public/voxduo-dev/www
PRD_RSYNC_TARGET_DIR=/home/blogs/public/voxduo/www

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make publish                     generate using production settings '
	@echo '   make ssh_upload                  upload the web site via SSH        '
	@echo '                                                                       '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html'
	@echo '                                                                       '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

docker_html:
	${BASEDIR}/build.sh

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

docker_publish:
	${BASEDIR}/betabuild.sh

publish_prd:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PRDCONF) $(PELICANOPTS)

docker_publish_prd:
	${BASEDIR}/prdbuild.sh

ssh_upload: docker_publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: docker_publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

ssh_prd_upload: docker_publish_prd
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(PRD_SSH_TARGET_DIR)

rsync_prd_upload: docker_publish_prd
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(PRD_SSH_TARGET_DIR) --cvs-exclude

rsync_copy: publish
	rsync -P -rvzc --delete $(OUTPUTDIR)/ $(RSYNC_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate serve devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
