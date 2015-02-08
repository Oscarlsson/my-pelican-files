#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oscar Carlsson'
SITENAME = u'Oscar techblog'
SITEURL = 'http://oscarlsson.se'
# When testing locally, set ''
# to get links right
#SITEURL = ''
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = "True"

# Feed generation is usually not desired when developing
FEED_RSS = "feeds/rss.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://www.github.com/oscarlsson'),
          ('linkedin', 'http://se.linkedin.com/pub/oscar-carlsson/63/3b7/801'),
#          ('twitter', 'http://www.twitter.com/oscarlsson'),
#          ('tumblr', 'http://oscarlsson.tumblr.com/'),
#          ('facebook', 'http://www.facebook.com/oscarlsson'),
          ('rss', SITEURL + '/feeds/rss.xml'))
FAVICON = SITEURL + '/images/favicon.png'
DEFAULT_PAGINATION = 10
THEME = "../pelican-themes/SoMABlog"

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar', "disqus_static"]

DISQUS_SITENAME = u'oscarstechblog'

SITETAGLINE = "a developer's blog"
DELETE_OUTPUT_DIRECTORY = False
TWITTER_USERNAME = "oscarlsson"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GRAVATAR = "http://0.gravatar.com/avatar/02f4f9c3b8c6f44c426f659283785634"
