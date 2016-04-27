import requests
import config

GITHUB_API_URL = 'https://api.github.com/'

if __name__ == '__main__':

    test = requests.get(GITHUB_API_URL,
                        auth=(config.GITHUB_USER,config.GITHUB_PWD))

    print(test.status)
    print(test.content)

    print('Testing GitHub API')