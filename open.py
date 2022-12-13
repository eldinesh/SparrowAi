import yaml, json
import openai
import random
from twitter import *

# Generate the prompt
def genPrompt():
    with open('seeds.yaml') as f:
        prompt = yaml.load(f, Loader=yaml.FullLoader)
        
    return(random.choice(prompt['seeds']))

# Generate the hashtags
def genHashTag(prompt):
    with open('seeds.yaml') as f:
        hash = yaml.load(f, Loader=yaml.FullLoader)

    if prompt == hash['seeds'][0]:
        hashtags = hash['hashtags'][0]
    elif prompt == hash['seeds'][1]:
        hashtags = hash['hashtags'][1]
    elif prompt == hash['seeds'][2]:
        hashtags = hash['hashtags'][2]
    
    return hashtags

# Load the eggs
def loadEggs(path, tweets):
    with open(path, 'r') as f:
        eggs = json.load(f)
        for egg in eggs:
            tweets.append(egg)
    return tweets

# Save the eggs
def saveEggs(path, tweets):
    with open(path, 'w') as f:
        json.dump(tweets, f)

# Generate and Validate the content and tweet it
def validateContent(api_key, engine, prompt, file, tweets, client):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.9,
        max_tokens=280,
        n=1,
        frequency_penalty=0,
        presence_penalty=1
    )
    response = response['choices'][0]['text'].strip('\n')

    # Loading the eggs
    loadEggs(file, tweets)

    # Check if the content is unique
    if response in tweets:
        print("Duplicate")
        validateContent(api_key, engine, prompt, file, tweets)
    else:
        print("Unique")

        # Generate the tweet
        response = response + "\n\n" + genHashTag(prompt)
        
        # Tweet the content
        tweetStatus = postStatus(client, response)

        if tweetStatus == 200:
            print('Tweeted: ' + response)
            tweets.append(response)
            saveEggs(file, tweets)

        else:
            print('Error: ' + str(tweetStatus))
        