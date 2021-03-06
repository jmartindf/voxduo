#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Vox Duo'
SITENAME = 'Vox Duo'
SITE_DESCRIPTION = 'is where Adam &amp; Joe talk about what interests them, for the enjoyment of an international audience.'
SITEURL = 'http://ego.home.thosemartins.family/~jmartin/voxpel'
TWITTER_URL = 'https://twitter.com/FromVoxDuo'

ENTERTAINED_LOGO = 'theme/media/Entertained%20Logo.jpg'
REACQUAINTED_LOGO = 'theme/media/Reacquainted%20Logo.jpg'
GOLDENAGE_LOGO = 'theme/media/Golden%20Age%20Logo2.jpg'
MASTER_FEED_LOGO = 'theme/media/Vox%20Duo%20Generic%20Show%20Art%20Logo.jpg'

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
    'pelican-podcast-feed',
    'category_meta'
]

THEME = 'themes/voxduo'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = None

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
CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'

PAGINATION_PATTERNS = (#
	(1, '{base_name}/', '{base_name}/index.html'),
	(2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Disable unneeded pages
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''


# Category Slug Fixes
CATEGORY_SUBSTITUTIONS = (('The Golden Age', 'goldenage', True),)

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
PODCAST_FEED_IMAGE = '%s/%s' % (SITEURL, MASTER_FEED_LOGO)
PODCAST_FEED_OWNER_NAME = 'Vox Duo'
PODCAST_FEED_OWNER_EMAIL = 'duo@voxduo.com'
PODCAST_FEED_CATEGORY = ['Society & Culture', 'Personal Journals']

# Feed for each podcast
PODCASTS = {
	'goldenage': {
		'PODCAST_FEED_PATH': u'goldenage.rss',
		'PODCAST_FEED_TITLE': u'The Golden Age',
		'PODCAST_FEED_EXPLICIT': u'No',
		'PODCAST_FEED_LANGUAGE': u'en-us',
		'PODCAST_FEED_COPYRIGHT': u'Copyright 2017-{0} {1}'.format(
		    datetime.now().year, AUTHOR),
		'PODCAST_FEED_SUBTITLE': u"We've never had more high quality ways to be entertained.",
		'PODCAST_FEED_AUTHOR': u'Vox Duo',
		'PODCAST_FEED_SUMMARY': u"""Have we ever had it so good? Not if you ask Adam and Joe, the vainglorious Vox Duo — and they intend to prove it by spotlighting the best of today’s movies, comics, and more! Join them in their Scrooge McDuck-like dive into a glittering hoard of entertainment options.""",
		'PODCAST_FEED_OWNER_NAME': 'Vox Duo',
		'PODCAST_FEED_OWNER_EMAIL': 'duo@voxduo.com',
		'PODCAST_FEED_CATEGORY': ('TV & Film', 'Games & Hobbies'),
		'PODCAST_FEED_NEWURL': 'https://files.voxduo.com/goldenage.rss'
	},
	'reacquainted': {
		'PODCAST_FEED_PATH': u'reacquainted.rss',
		'PODCAST_FEED_TITLE': u'Reacquainted',
		'PODCAST_FEED_EXPLICIT': u'No',
		'PODCAST_FEED_LANGUAGE': u'en-us',
		'PODCAST_FEED_COPYRIGHT': u'Copyright 2017-{0} {1}'.format(
		    datetime.now().year, AUTHOR),
		'PODCAST_FEED_SUBTITLE': u'What in the world happened to you?',
		'PODCAST_FEED_AUTHOR': u'Vox Duo',
		'PODCAST_FEED_SUMMARY': u"Adam and Joe were childhood friends, but life pulled them apart. 20 years later, they're very different people.",
		'PODCAST_FEED_OWNER_NAME': 'Vox Duo',
		'PODCAST_FEED_OWNER_EMAIL': 'duo@voxduo.com',
	},
	'entertained': {
		'PODCAST_FEED_PATH': u'entertained.rss',
		'PODCAST_FEED_TITLE': u'Are You Not Entertained?',
		'PODCAST_FEED_EXPLICIT': u'No',
		'PODCAST_FEED_LANGUAGE': u'en-us',
		'PODCAST_FEED_COPYRIGHT': u'Copyright 2017-{0} {1}'.format(
		    datetime.now().year, AUTHOR),
		'PODCAST_FEED_SUBTITLE': u'Occasional movie reviews, from the Vox Duo crew.',
		'PODCAST_FEED_AUTHOR': u'Vox Duo',
		'PODCAST_FEED_SUMMARY': u"An occasional show, to talk about entertainment. But mostly movies.",
		'PODCAST_FEED_OWNER_NAME': 'Vox Duo',
		'PODCAST_FEED_OWNER_EMAIL': 'duo@voxduo.com',
	}
}

PODCASTS['entertained']['PODCAST_FEED_IMAGE'] = '%s/%s' % (SITEURL, ENTERTAINED_LOGO)
PODCASTS['reacquainted']['PODCAST_FEED_IMAGE'] = '%s/%s' % (SITEURL, REACQUAINTED_LOGO)
PODCASTS['goldenage']['PODCAST_FEED_IMAGE'] = '%s/%s' % (SITEURL, GOLDENAGE_LOGO)

def duration_filter(value):
	if value.count(":") > 0:
		pieces = value.split(":")
		if len(pieces) == 3:
			return str((int(pieces[0])*60)+int(pieces[1]))
		elif len(pieces) == 2:
			return pieces[0]
		else:
			return "0"
	else:
		return "0"

JINJA_FILTERS = {'enjoyment': duration_filter}
