import fitbit
import config
import requests

# Based upon a modified version of Paul Weeks' example
# http://pdwhomeautomation.blogspot.co.uk/2016/01/fitbit-api-access-using-oauth20-and.html

authd_client = fitbit.Fitbit('<consumer_key>', '<consumer_secret>',
                             access_token='<access_token>', refresh_token='<refresh_token>')

AUTH_URI = 'https://www.fitbit.com/oauth2/authorize'


'''
Example from FitBit Developer Documentation to get Authorization Code
https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=22942C&redirect_uri=http%3A%2F%2Fexample.com%2Fcallback&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight
'''




if __name__ == '__main__':

    # Requesting an authorization code
    stuff = requests.get('https://www.fitbit.com/oauth2/authorize',
                         params = {'response_type': 'code',
                                   'client_id': config.FITBIT_CONSUMER_KEY,
                                   'redirect_uri': 'http://example.com',
                                   'callback': '',
                                   'scope': ['activity','nutrition','settings','sleep','weight']})

    print(stuff.content)
    print(stuff.url)

    # Not quite sure whether this can be used rather than having to send explicit requests
    test = fitbit.FitbitOauth2Client(config.FITBIT_CONSUMER_KEY, config.FITBIT_CONSUMER_SECRET)
    #auth = test.authorize_token_url()
    print(test)

    print('Testing FitBit package')