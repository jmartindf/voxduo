#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Vox Duo'
SITENAME = 'Vox Duo Podcasts'
SITEURL = 'https://beta.voxduo.com'

PATH = 'content'
STATIC_PATHS = [
    'audio',
    'images',
]
ARTICLE_PATHS = ['./episodes']

PLUGIN_PATHS = ['./plugins', './pelican-plugins', ]
PLUGINS = [
    'summary',
    'feed_summary',
    'pelican-podcast-feed'
]

THEME = 'themes/notmyidea'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('@FromVoxDuo', 'https://twitter.com/FromVoxDuo'),
        ('@jmartindf', 'https://twitter.com/jmartindf'),
        ('@AdamVolle', 'https://twitter.com/AdamVolle'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URLs
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}'
CATEGORY_URL = '{slug}/archive.html'
CATEGORY_SAVE_AS = '{slug}/archive.html'

# Category Slug Fixes
CATEGORY_SUBSTITUTIONS = (('Are You Not Entertained?', 'entertained', True),)

# iTunes plugin settings
PODCAST_FEED_PATH = u'podcast.rss'
PODCAST_FEED_TITLE = u'Vox Duo Podcasts'
PODCAST_FEED_EXPLICIT = u'No'
PODCAST_FEED_LANGUAGE = u'en-us'
PODCAST_FEED_COPYRIGHT = u'Copyright 2017-{0} {1}'.format(
    datetime.now().year, AUTHOR)
PODCAST_FEED_SUBTITLE = u'The voice of two people'
PODCAST_FEED_AUTHOR = u'Vox Duo'
PODCAST_FEED_SUMMARY = u''
PODCAST_FEED_IMAGE = 'https://beta.voxduo.com/images/Reacquainted%20Logo.jpg'
PODCAST_FEED_OWNER_NAME = 'Vox Duo'
PODCAST_FEED_OWNER_EMAIL = 'duo@voxduo.com'
PODCAST_FEED_CATEGORY = ['Society & Culture', 'Personal Journals']
