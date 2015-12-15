#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brendan Horan'
SITENAME = 'Blog'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'en'

# disable all feeds for local dev site
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable author pages
AUTHOR_SAVE_AS = ''

# What theme to set
THEME = 'theme/pelican-bootstrap3'

# Enable plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['pelican_comment_system', 'tipue_search']

# The following templages need tp be generated for the search to work
DIRECT_TEMPLATES = (('categories', 'archives', 'search', 'index'))

# Disable categories from the top menu
DISPLAY_CATEGORIES_ON_MENU = False

# Links for the social menus in the sidebar
SOCIAL =  (('Github', 'https://github.com/brendanhoran'),
          ('Linkedin', 'https://hk.linkedin.com/in/brendan-horan-0910083'),)

# Set site wide license 
CC_LICENSE = "CC-BY"

# Disable article tags from appearing in sidebar
DISPLAY_TAGS_ON_SIDEBAR = False

# Display article categories in sidebar
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# Enable the static comment system, only for articles
PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_FEED = None
PELICAN_COMMENT_SYSTEM_FEED_ALL = None

# Code block style
PYGMENTS_STYLE = 'default'
# Set pygments options to disable all syntax highlights by default
MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=default, guess_lang=false)', 'extra']

# Number of articles per page
DEFAULT_PAGINATION = 10
