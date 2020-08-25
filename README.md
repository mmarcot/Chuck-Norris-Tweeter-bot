# Twitter bot that spread Chuck Norris jokes

This is a basic Twitter bot that get jokes from an API http://www.icndb.com/api/ and tweet them around.

It needs to be lied to a existing dev Twitter account. The bot randomly choose a person that you are following and comment his last tweet with a random joke from the API.

## Installation

create a keys.py file in the project directory containg following variables (replace XXX with your Twitter API keys):
    api_key = "XXX"
    api_secret_key = "XXX"
    access_token = "XXX"
    access_token_secret = "XXX"

    pip install tweepy
    python keys.py
