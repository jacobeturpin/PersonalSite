import fitbit
import config

# Based upon a modified version of Paul Weeks' example
# http://pdwhomeautomation.blogspot.co.uk/2016/01/fitbit-api-access-using-oauth20-and.html

authd_client = fitbit.Fitbit('<consumer_key>', '<consumer_secret>',
                             access_token='<access_token>', refresh_token='<refresh_token>')

AUTH_URI = 'https://www.fitbit.com/oauth2/authorize'


'''
Example from FitBit Developer Documentation to get Authorization Code
https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=22942C&redirect_uri=http%3A%2F%2Fexample.com%2Fcallback&scope=activity%20nutrition%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight
'''


# Sample Payload
{
'code' : AuthorizationCode,
'redirect_uri' : config.REDIRECT_URI,
'client_id' : config.CONSUMER_KEY,
'grant_type' : 'authorization_code'
}




if __name__ == '__main__':
    print('Testing FitBit package')