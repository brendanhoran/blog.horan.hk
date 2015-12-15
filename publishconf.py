#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# set live site url
SITEURL = 'https://blog.horan.hk'

# Enable atom feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# append the rss link to the social sidebar
# you must use the VARIABLE syntax for the atom feed, vs the actual URL
SOCIAL = SOCIAL + (('RSS feed', SITEURL + '/' + FEED_ALL_ATOM , 'rss'),)

# disable for prod
RELATIVE_URLS = False

# delete "output" dir before regen
DELETE_OUTPUT_DIRECTORY = True
