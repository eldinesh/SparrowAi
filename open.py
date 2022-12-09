import yaml
import openai
import random

# Generate the content
def genText(api_key, engine, prompt):
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
    return response['choices'][0]['text'].strip('\n')

# Generate the prompt
def genPrompt():
    with open('seeds.yaml') as f:
        prompt = yaml.load(f, Loader=yaml.FullLoader)
        
    return('tell me a ' + random.choice(prompt['seeds']))
