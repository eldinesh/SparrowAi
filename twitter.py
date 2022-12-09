import tweepy

# Twitter Authenticaiton and API setup
def auth(api_key, api_key_secret, access_token, access_token_secret):
    client = tweepy.Client(consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token, access_token_secret=access_token_secret) 
    return client

# Twitter Stauts Update
def postStatus(client, data):
    client.create_tweet(text = data)
    return 200
    