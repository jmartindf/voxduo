#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from publishconf import *

SITEURL = 'https://voxduo.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

# Fix podcast feed image URL
PODCASTS['entertained']['PODCAST_FEED_IMAGE'] = '%s/%s' % (SITEURL, ENTERTAINED_LOGO)
PODCASTS['reacquainted']['PODCAST_FEED_IMAGE'] = '%s/%s' % (SITEURL, REACQUAINTED_LOGO)
PODCASTS['goldenage']['PODCAST_FEED_IMAGE'] = '%s/%s' % (SITEURL, GOLDENAGE_LOGO)
PODCAST_FEED_IMAGE = '%s/%s' % (SITEURL, MASTER_FEED_LOGO)
