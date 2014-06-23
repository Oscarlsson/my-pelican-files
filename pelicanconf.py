#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Oscar Carlsson'
SITENAME = u'Oscar techblog'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = "True"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "Test"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://www.github.com/oscarlsson'),
          ('linkedin', 'http://se.linkedin.com/pub/oscar-carlsson/63/3b7/801'),
          ('twitter', 'http://www.twitter.com/oscarlsson'),
          ('tumblr', 'http://www.tumblr.com/oscarlsson'),
          ('facebook', 'http://www.facebook.com/oscarlsson'))

DEFAULT_PAGINATION = 10
THEME = "../pelican-themes/SoMABlog"

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar', "disqus_static"]

DISQUS_SITENAME = u'oscarstechblog'

#SITESUBTITLE = "SK"
SITETAGLINE = "a developer's blog"
DELETE_OUTPUT_DIRECTORY = False
TWITTER_USERNAME = "oscarlsson"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GRAVATAR = "http://0.gravatar.com/avatar/02f4f9c3b8c6f44c426f659283785634"
