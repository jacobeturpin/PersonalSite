import fitbit
import config
import requests

# Based upon a modified version of Paul Weeks' example
# http://pdwhomeautomation.blogspot.co.uk/2016/01/fitbit-api-access-using-oauth20-and.html

authd_client = fitbit.Fitbit(config.FITBIT_CONSUMER_KEY, 
                             config.FITBIT_CONSUMER_SECRET,
                             access_token=config.FITBIT_ACCESS_TOKEN, 
                             refresh_token=config.FITBIT_REFRESH_TOKEN)




if __name__ == '__main__':

    test = authd_client.get_devices()
    print(test)

    print('Testing FitBit package')