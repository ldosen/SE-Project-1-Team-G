import unittest
from messageParser import *

class TestMessageParserFunctions(unittest.TestCase):

    def setUp(self):
        #TEST 1
        self.test1 = messageParser("@franky goes to #hollywood. See http://cnn.com")
        self.test1.extract_topics()
        self.test1.extract_mentions()
        self.test1.extract_urls()
        #TEST 2
        self.test2 = messageParser("@7 #7")
        self.test2.extract_topics()
        self.test2.extract_mentions()
        self.test2.extract_urls()
        #TEST 3 
        self.test3 = messageParser("If I hear one more #terribleraprecord @I am going to have to do it to those @meatballs")
        self.test3.extract_topics()
        self.test3.extract_mentions()
        self.test3.extract_urls()

    def tearDown(self):
        pass

    def test_Mention(self):
        #TEST 1
        self.assertTrue(self.test1.is_mentioned("franky"))
        self.assertFalse(self.test1.is_mentioned("george"))
        self.assertEqual(self.test1.times_mentioned("franky"), 1)
        self.assertEqual(self.test1.times_mentioned("george"), None)
        self.assertEqual(self.test1.total_mentions(), 1)
        #TEST 2
        self.assertTrue(self.test2.is_mentioned("7"))
        self.assertEqual(self.test2.times_mentioned("george"), None)
        self.assertEqual(self.test2.total_mentions(), 1)
        #TEST 3
        self.assertTrue(self.test3.is_mentioned("I"))
        self.assertFalse(self.test3.is_mentioned("meat"))
        self.assertEqual(self.test3.times_mentioned("meatballs"), 1)
        self.assertEqual(self.test3.times_mentioned("george"), None)
        self.assertEqual(self.test3.total_mentions(), 2)

    def test_Topic(self):
        #TEST 1
        self.assertTrue(self.test1.has_topic("hollywood"))
        self.assertFalse(self.test1.has_topic("redcarpet"))
        self.assertEqual(self.test1.total_topics(), 1)
        #TEST 2
        self.assertTrue(self.test2.has_topic("7"))
        self.assertEqual(self.test2.total_topics(), 1)
        #TEST 3
        self.assertTrue(self.test1.has_topic("terribleraprecord"))
        self.assertFalse(self.test1.has_topic("rap"))
        self.assertEqual(self.test1.total_topics(), 1)

    def test_URL(self):
        #TEST 1
        self.assertTrue(self.test1.is_referenced("http://cnn.com"))
        self.assertEqual(self.test1.totalURL(), 1)
        #TEST 2
        self.assertFalse(self.test2.is_referenced("http://cnn.com"))
        self.assertEqual(self.test2.totalURL(), 0)
        #TEST 3
        self.assertFalse(self.test1.is_referenced("http://cnn.com"))
        self.assertEqual(self.test1.totalURL(), 0)
        
if __name__ == '__main__':
    unittest.main()
    