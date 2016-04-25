from twitter import *
from config import *


def get_twitter_data():

    t = Twitter(auth=OAuth(TWITTER_ACCESS_TOKEN, 
                           TWITTER_ACCESS_TOKEN_SECRET,
                           TWITTER_CONSUMER_KEY, 
                           TWITTER_CONSUMER_SECRET))
    profile = t.account.verify_credentials()
    tweets = t.statuses.user_timeline(count=5)

    return profile, tweets


if __name__ == '__main__':
    
    t = Twitter(auth=OAuth(TWITTER_ACCESS_TOKEN, 
                           TWITTER_ACCESS_TOKEN_SECRET,
                           TWITTER_CONSUMER_KEY, 
                           TWITTER_CONSUMER_SECRET))
    test_profile = t.account.verify_credentials()
    test_tweets = t.statuses.user_timeline(count=5)

    print(test_profile)
    print(test_tweets[4])