# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://soringherghisan.github.io/pelican_blog'
RELATIVE_URLS = False

# Update menu links to include SITEURL
MENUITEMS = (
    ("Archives", SITEURL + "/archives.html"),
    ("Categories", SITEURL + "/categories.html"),
)

# Update logo/favicon paths
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
