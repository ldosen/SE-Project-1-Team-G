import re

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

    def is_mentioned(self, username):
        pass

    def times_mentioned(self, mention):
        pass

    def total_mentions(self):
        pass

    def has_topic(self, topic):
        if topic in self.topics.keys():
            return True
        else:
            return False

    def total_topics(self):
        return len(self.topics.keys())

    def is_referenced(self, url):
        pass

    def totalURL(self):
        pass

