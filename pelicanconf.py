#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Stephen DiCato'
SITENAME = u'stephendicato.com'
SITEURL = ''

THEME = 'simple-bootstrap'

# Appliy the typogrify improvements.
# TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# This is a hack to make the author URLs link to my about page (without
# modifying the template).
AUTHOR_URL = 'pages/about.html'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = '%m/%d/%Y %I:%M %p EST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('email', 'mailto:stephendicato@gmail.com'),
          ('linkedin', 'https://www.linkedin.com/in/stephendicato'),
          ('github', 'https://github.com/dicato'),)

DEFAULT_PAGINATION = False
# Change the default URLs.
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

# Set up locations of articles, pages and theme.
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# Set up static content and output locations.
STATIC_PATHS = [
    'images',
    'static'
]
EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
}
TEMPLATE_PAGES = {
    # Custom 404 page for GitHub pages.
    '404.html': '404.html',
}
