import tweepy
import requests
import time
import random
import html
from keys import api_key, api_secret_key, access_token, access_token_secret


TWITTER_CHAR_LIMIT = 280
SLEEP_TIME_BETWEEN_TWEETS = 60 # in seconds


# twitter API auth:
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print('Logged in')


def get_joke():
    joke = 'a' * (TWITTER_CHAR_LIMIT + 1)
    while len(joke) >= TWITTER_CHAR_LIMIT:
        print("Getting a Chuck joke")
        response = requests.get('http://api.icndb.com/jokes/random/')
        data = response.json()
        joke = data['value']['joke']
    return html.unescape(joke)

while True:
    # pick a random friend:
    friends = api.friends()
    friend = random.choice(friends)
    print('Target ready --> {}'.format(friend.name))

    # get his last tweet:
    tweet = api.user_timeline(friend.id, count=1)[0]
    print('Tweet found')

    reply = get_joke()
    print('Reply built :: {}'.format(reply))
    res = api.update_status(reply, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    print("Tweeted !")

    time.sleep(SLEEP_TIME_BETWEEN_TWEETS)
