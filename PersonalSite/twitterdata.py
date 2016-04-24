import twitter
from config import *


''' ---------------------- '''
''' PYTHON-TWITTER PACKAGE '''
''' ---------------------- '''
'''
api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    print(api)

    test = api.GetUserTimeline()
    print(test)
'''


''' --------------- '''
''' TWITTER PACKAGE '''
''' --------------- '''

if __name__ == '__main__':
    
    t = twitter.Twitter(auth=twitter.OAuth(TWITTER_ACCESS_TOKEN, 
                                           TWITTER_ACCESS_TOKEN_SECRET,
                                           TWITTER_CONSUMER_KEY, 
                                           TWITTER_CONSUMER_SECRET))
    test = t.statuses.home_timeline()
    print(len(test))
    print(test[0]['user'])