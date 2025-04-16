from datetime import datetime

AUTHOR = 'This freaking guy, huh?'
SITEURL = ""
SITENAME = 'Pelican Docs Tutorial'
SITETITLE = 'Gherghisian Sorinian'
SITESUBTITLE = 'Generalist'

BROWSER_COLOR = '#d6a691'       # todo: # what does this do ? doesn't seem to have any effect
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/favicon.ico'

PATH = 'content'
ROBOTS = 'index, follow'
OUTPUT_PATH = 'output/'

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'English'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
)

COPYRIGHT_YEAR = datetime.now().year

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ("Pelican 🦃", "https://getpelican.com/"),
    ("Python.org 🐍", "https://www.python.org/"),
    ("Jinja2 📑", "https://palletsprojects.com/p/jinja/"),
)

SOCIAL = (
    ('github', 'https://github.com/soringherghisan/'),
    ('linkedin', 'https://www.linkedin.com/in/sorin-gherghisan-434106194')
)

DEFAULT_PAGINATION = 10

STATIC_CHECK_IF_MODIFIED = True     # todo: check what this does

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# seems this options is needed for fixing various settings problems,
# although it's not added by default
LOAD_CONTENT_CACHE = False

# For Flex Theme # some taken from ` downloaded_themes/Flex/docs/pelicanconf.py `
# not sure if some of the above are not also theme specific - will have to check
THEME = 'Flex'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike 4.0 International License',
    'version': '4.0',
    'slug': 'by-sa',
    'icon': True,
    'language': 'en_US',
}
