import unittest
from messageParser import *

class TestMessageParserFunctions(unittest.TestCase):

    def setUp(self):
        self.parser = messageParser("@franky goes to #hollywood. See http://cnn.com")
        self.parser.extract_topics()
        self.parser.extract_mentions()

    def testMention(self):
        self.assertTrue(self.parser.is_mentioned("franky"))
        self.assertFalse(self.parser.is_mentioned("george"))
        self.assertEqual(self.parser.times_mentioned("franky"), 1)
        self.assertEqual(self.parser.times_mentioned("george"), None)
        self.assertEqual(self.parser.total_mentions(), 1)

    def testTopic(self):
        self.assertTrue(self.parser.has_topic("hollywood"))
        self.assertFalse(self.parser.has_topic("redcarpet"))
        self.assertEqual(self.parser.total_topics(), 1)

    def testURL(self):
        self.assertTrue(self.parser.is_referenced("http://cnn.com"))
        self.assertEqual(self.parser.totalURL(), 1)
