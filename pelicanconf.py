#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'king6cong'
SITENAME = u'Bungeer'
SITEURL = 'http://127.0.0.1:8000'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

DEFAULT_DATE='fs'
PDF_GENERATOR=True

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'cn': '%Y-%m-%d(%a)',
}

TYPOGRIFY=True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_MAX_ITEMS = 60

# THEME = "notmyidea"
# THEME = "/Users/cong/code/pelican-themes/bluegrasshopper"
# THEME = "/Users/cong/code/pelican-themes/Just-Read"

# THEME = "/Users/cong/code/pelican-themes/bootstrap2"
# THEME = "/Users/cong/code/pelican-themes/dev-random2"
#THEME = "/Users/cong/code/pelican-themes/"


#THEME = "/Users/cong/code/pelican-themes/Just-Read"
#THEME = "/Users/cong/code/pelican-themes/basic"
#THEME = "/Users/cong/code/pelican-themes/bluegrasshopper"
#THEME = "/Users/cong/code/pelican-themes/bold"
#THEME = "/Users/cong/code/pelican-themes/bootlex"
#THEME = "/Users/cong/code/pelican-themes/bootstrap"
#THEME = "/Users/cong/code/pelican-themes/bootstrap2"
#THEME = "/Users/cong/code/pelican-themes/brownstone"
#THEME = "/Users/cong/code/pelican-themes/built-texts"
#THEME = "/Users/cong/code/pelican-themes/cebong"
#THEME = "/Users/cong/code/pelican-themes/chunk"
#THEME = "/Users/cong/code/pelican-themes/crowsfoot"
#THEME = "/Users/cong/code/pelican-themes/dev-random"
#THEME = "/Users/cong/code/pelican-themes/dev-random2"
#THEME = "/Users/cong/code/pelican-themes/elegant"
#THEME = "/Users/cong/code/pelican-themes/fresh"
#THEME = "/Users/cong/code/pelican-themes/gum"
#THEME = "/Users/cong/code/pelican-themes/html5-dopetrope"
#THEME = "/Users/cong/code/pelican-themes/irfan"
#THEME = "/Users/cong/code/pelican-themes/iris"
#THEME = "/Users/cong/code/pelican-themes/jesuislibre"
#THEME = "/Users/cong/code/pelican-themes/lannisport"
#THEME = "/Users/cong/code/pelican-themes/lightweight"
#THEME = "/Users/cong/code/pelican-themes/martyalchin"
#THEME = "/Users/cong/code/pelican-themes/mnmlist"
#THEME = "/Users/cong/code/pelican-themes/monospace"
#THEME = "/Users/cong/code/pelican-themes/neat"
#THEME = "/Users/cong/code/pelican-themes/niu-x2"
#THEME = "/Users/cong/code/pelican-themes/nmnlist"
#THEME = "/Users/cong/code/pelican-themes/notmyidea-cms"
#THEME = "/Users/cong/code/pelican-themes/notmyidea-cms-fr"
#THEME = "/Users/cong/code/pelican-themes/pelican-bootstrap3"
#THEME = "/Users/cong/code/pelican-themes/pelican-cait"
#THEME = "/Users/cong/code/pelican-themes/pelican-mockingbird"
#THEME = "/Users/cong/code/pelican-themes/pelipress"
#THEME = "/Users/cong/code/pelican-themes/plumage"
#THEME = "/Users/cong/code/pelican-themes/pure"
#THEME = "/Users/cong/code/pelican-themes/relapse"
#THEME = "/Users/cong/code/pelican-themes/sneakyidea"
#THEME = "/Users/cong/code/pelican-themes/storm"
#THEME = "/Users/cong/code/pelican-themes/subtle"
#THEME = "/Users/cong/code/pelican-themes/sundown"
#THEME = "/Users/cong/code/pelican-themes/svbhack"
#THEME = "/Users/cong/code/pelican-themes/svbtle"
#THEME = "/Users/cong/code/pelican-themes/syte"
#THEME = "/Users/cong/code/pelican-themes/tuxlite_tbs"
#THEME = "/Users/cong/code/pelican-themes/tuxlite_zf"
#THEME = "/Users/cong/code/pelican-themes/water-iris"
#THEME = "/Users/cong/code/pelican-themes/waterspill"
#THEME = "/Users/cong/code/pelican-themes/waterspill-en"
#THEME = "/Users/cong/code/pelican-themes/"


#THEME = "/Users/cong/code/pelican-themes/sneakyidea"
#THEME = "/Users/cong/code/pelican-themes/pelipress"
#THEME = "/Users/cong/code/pelican-themes/plumage"
#THEME = "/Users/cong/code/pelican-themes/mnmlist"
#THEME = "/Users/cong/code/pelican-themes/martyalchin"
#THEME = "/Users/cong/code/pelican-themes/iris"
#THEME = "/Users/cong/code/pelican-themes/niu-x2"
#THEME = "/Users/cong/code/pelican-themes/monospace"

#THEME = "/Users/cong/code/pelican-themes/chunk"
#THEME = "/Users/cong/code/pelican-themes/crowsfoot"
#THEME = "/Users/cong/code/pelican-themes/dev-random"
#THEME = "/Users/cong/code/pelican-themes/dev-random2"
#THEME = "/Users/cong/code/pelican-themes/elegant"


#THEME = "/Users/cong/code/pelican-themes/html5-dopetrope"
#THEME = "/Users/cong/code/pelican-themes/lannisport"
#THEME = "/Users/cong/code/pelican-themes/nmnlist"


#THEME = "/Users/cong/code/pelican-themes/fresh"
#THEME = "/Users/cong/code/pelican-themes/pelican-cait"
#THEME = "/Users/cong/code/pelican-themes/pelican-mockingbird"
#THEME = "/Users/cong/code/pelican-themes/pure"
#THEME = "/Users/cong/code/pelican-themes/subtle"
#THEME = "/Users/cong/code/pelican-themes/waterspill-en"
#THEME = "/Users/cong/code/pelican-themes/pelican-bootstrap3"
THEME = "/Users/cong/code/pelican-themes/gum"

#THEME_STATIC_PATHS=['/Users/cong/code/pelican-themes/lannisport/static']

# Blogroll
LINKS =  (('Bungeer视频', 'http://bungeer.com/'),
          ('Bungeer安卓版', 'http://bungeer.com/android'),
          )

# Social widget
SOCIAL = (('新浪微博', 'http://weibo.com/u/2516756763'),
          ('腾讯微博', 'http://t.qq.com/king6cong'),)

DEFAULT_PAGINATION = 6

DISQUS_SITENAME='bungeer'
GOOGLE_ANALYTICS='UA-44864814-1'

GITHUB_URL='https://github.com/king6cong'
TWITTER_USERNAME='king6cong'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
