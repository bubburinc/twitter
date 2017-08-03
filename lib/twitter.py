# delete tweets

import tweepy


class Twitter(object):
    _api = None

    def __init__(self, access_token_secret, consumer_secret, consumer_key,
                 access_token):
        self.consumer_secret = consumer_secret
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.access_token = access_token
        self.__auth_handler()

    def __auth_handler(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self._api = tweepy.API(auth)

    def clean_up(self):
        # Pull in all tweets from the users timeline
        timeline = tweepy.Cursor(self._api.user_timeline, count=200).items()

        deletion_count = 0
        for tweet in timeline:
            # Where tweets are not in save list and older than cutoff date
            if tweet.id:
                self._api.destroy_status(tweet.id)
                print("Deleted %d: [%s] %s" % (
                    tweet.id, tweet.created_at, tweet.text))
                deletion_count += 1
        print("Deleted %d tweets " % (deletion_count))



