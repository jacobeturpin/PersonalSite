import fitbit

authd_client = fitbit.Fitbit('<consumer_key>', '<consumer_secret>',
                             access_token='<access_token>', refresh_token='<refresh_token>')


if __name__ == '__main__':
    print('Testing FitBit package')