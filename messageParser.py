import re
import argparse
from urllib.parse import urlparse

class messageParser(object):

    def __init__(self, message):
        self.message = message
        self.topics = {}
        self.mentions = {}
        self.links = {}

    def extract_topics(self):
        hashtag_re = re.compile("(?:^|\s)[＃#]{1}(\w+)", re.UNICODE)
        extracted_topics = hashtag_re.findall(self.message)
        for i in extracted_topics:
            topic = i
            if topic not in self.topics.keys():
                self.topics.setdefault(topic, 1)
            else:
                self.topics[topic] += 1

    def extract_mentions(self):
        mention_re = re.compile("(?:^|\s)[＠ @]{1}([^\s#<>[\]|{}]+)", re.UNICODE)
        extracted_mentions = mention_re.findall(self.message)
        for i in extracted_mentions:
            mention = i
            if mention not in self.mentions.keys():
                self.mentions.setdefault(mention, 1)
            else:
                self.mentions[mention] += 1

    def extract_urls(self):
        url_re = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.UNICODE)
        extracted_urls = url_re.findall(self.message)
        for i in extracted_urls:
            url = i
            if url not in self.links.keys():
                self.links.setdefault(url, 1)
            else:
                self.links[url] += 1


    def is_mentioned(self, username):
        if username in self.mentions.keys():
            return True
        else:
            return False

    def times_mentioned(self, mention):
        return self.mentions.get(mention)

    def total_mentions(self):
        return len(self.mentions.keys())

    def has_topic(self, topic):
        if topic in self.topics.keys():
            return True
        else:
            return False

    def total_topics(self):
        return len(self.topics.keys())

    def is_referenced(self, url):
        if url in self.links.keys():
            return True
        else:
            return False

    def totalURL(self):
        return len(self.links.keys())
