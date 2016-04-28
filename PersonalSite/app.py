"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import twitterdata

from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', name='Jacob Turpin')


@app.route('/GetTwitterData')
def twitter_data():
    profile, tweets = twitterdata.get_twitter_data()
    return jsonify(profile_data = profile,
                   tweet_data = tweets)

@app.route('/GetFitBitData')
def fitbit_data():
    return "FitBit Data Goes Here"


@app.route('/GetGitHubData')
def github_data():
    return "GitHub Data Goes Here"


@app.route('/GetLinkedInData')
def linkedin_data():
    return "LinkedIn Data Goes Here"


@app.route('/test')
def hello():
    ''' Simple route left purely for identifying whether it's possible to successfully reach the site ''' 
    return "Testing"


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
