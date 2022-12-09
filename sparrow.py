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
locNest = 'nest/eggs.txt'

# Twitter Authenticaiton and client setup
client = auth(api_key, api_key_secret, access_token, access_token_secret)

# Generate the prompt
prompt = genPrompt()

# Generate the content
data = genText(open_api_key, open_engine, prompt)

# Tweet the content
response = postStatus(client, data)

if response == 200:
    print('Tweeted: ' + data)
    
    with open(locNest, 'a') as f:
        f.write(data)

else:
    print('Error: ' + str(response))