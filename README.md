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

## Work flow for a new plug post
This section makes use of the included "Makefile".     
Only change to the Makefile was :   
```
SSH_HOST= blog.horan.hk
SSH_PORT= 22
SSH_USER= oldmate
SSH_TARGET_DIR= /dev/null
```


1) Write a new article.     
   vim content/2015-12-12.new-blog-post.mk      
   The header should contain the follwoing :     
   ```
   title: Check out my new post
   Category:  howto
   Slug: check-my-post
   date: 2015-12-12
   summary: How to write the headers for a new post on my blog
   ```
2) Test it localy     
  run : "make html"     
  run : "make serve"    
  View in web browser "http://localhost:8000"    
  
3) Publish to web server    
  run : "make publish"   
  run : "make rsync_upload"    
  Done   

