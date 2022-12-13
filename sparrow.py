import os

from twitter import *
from open import *

# Set the variables
open_api_key = os.environ['open_api_key']
open_engine = os.environ['open_engine']
api_key = os.environ['api_key']
api_key_secret = os.environ['api_key_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Specify the path
locNest = 'nest/eggs.json'

# Twitter Authenticaiton and client setup
client = auth(api_key, api_key_secret, access_token, access_token_secret)

# Temporary list to hold the tweets
tweets = []

# Generate the prompt
prompt = genPrompt()

# Generate the content and tweet it
validateContent(open_api_key, open_engine, prompt, locNest, tweets, client)