'''
    Module used to search in Twitter
'''
from twython import Twython

class TwitterSearcher(object):
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.twitter_api = Twython(consumer_key,
                                   consumer_secret,
                                   token_key,
                                   token_secret)

    def search(self, text, since_id=None):
        if self.twitter_api is None:
            raise Exception('Not authenticated')
        # 100 because it is the maximum for non-premnium
        return self.twitter_api.search(q=text, count=100, since_id=since_id)

    def user_search(self, text):
        if self.twitter_api is None:
            raise Exception('Not authenticated')
        return self.twitter_api.search_users(q=text)

