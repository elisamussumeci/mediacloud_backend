#-*- coding:utf-8 -*-
u"""
Created on 24/04/14
by fccoelho
license: GPL V3 or Later
"""

__docformat__ = 'restructuredtext en'

import unittest
import datetime

import pymongo

from analysis import htod


class TestFreqdist(unittest.TestCase):
    """
    Writing tests for this is hard because it takes a long time to calculate the freqdist file.
    """
    pass

class TestHtod(unittest.TestCase):
    def setUp(self):
        htod.client = pymongo.MongoClient('localhost', 27017)
        htod.ARTICLES = htod.client.MCDB.articles

    def test_fetch_today_articles(self):
        d = "2014-02-14"
        arts = list(htod.fetch_articles(d))
        self.assertGreater(len(arts), 0)
        for a in arts:
            self.assertGreaterEqual(a["published"], datetime.datetime(2014, 02, 14))
            self.assertLess(a["published"], datetime.datetime(2014, 02, 15))
