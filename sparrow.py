import configparser

from twitter import *
from open import *

# Read the config file and set the variables
config = configparser.ConfigParser()
config.read('config.ini')
open_api_key = config['open']['open_api_key']
open_engine = config['open']['open_engine']
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
client_id = config['twitter']['client_id']
client_secret = config['twitter']['client_secret']

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