from datetime import datetime

AUTHOR = 'This freaking guy, huh?'
SITEURL = ""
SITENAME = 'Pelican Docs Tutorial'
SITETITLE = 'Gherghisian Sorinian'
SITESUBTITLE = 'Generalist'

BROWSER_COLOR = '#d6a691'  # todo: # what does this do ? doesn't seem to have any effect
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/images/favicon.ico'

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
)

DEFAULT_PAGINATION = 10

STATIC_CHECK_IF_MODIFIED = True  # todo: check what this does

LOAD_CONTENT_CACHE = False

# For Flex Theme # some taken from ` downloaded_themes/Flex/docs/pelicanconf.py `
# not sure if some of the above are not also theme specific - will have to check
THEME = './theme/Flex'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike 4.0 International License',
    'version': '4.0',
    'slug': 'by-sa',
    'icon': True,
    'language': 'en_US',
}
