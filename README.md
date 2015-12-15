# Pelican configs/themes/plugins for blog.horan.hk

## Overview

This git repo holds the config files, theme files and plugin files I use to generate the site blog.horan.hk.

### Directory overview


* README.md -- This file
* pelicanconf.py -- Pelican config + dev settings
* publishconf.py -- Pelican config (inherited) + prod settings
* plugins
  * tipue_search.py -- Tipue search plugin
  * pelican_comment_system -- Static pelican comment plugin (unmodified from upstream)
* theme
  * pelican-bootstrap3 -- My current theme (modified from upstream)

### Details on modfictions

* pelicanconf.py and publishconf.py are fully commented in-line, please see each file for the meaning of each setting.
* pelican-bootstrap3
  * Ripped out any social media rubbish (facebook, twitter etc) [Ongoing effort]
  * Updated tipue search to v5 to resolve search page generation issue
