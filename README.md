# SparrowAi

SparrowAi is a Twitter project that uses the OpenAI API model davinci-03 to generate content for tweets. The project uses the tweepy module to authenticate with a Twitter account and post the generated tweets. 

[![run sparrow.py](https://github.com/eldinesh/SparrowAi/actions/workflows/actions.yml/badge.svg)](https://github.com/eldinesh/SparrowAi/actions/workflows/actions.yml)



## Prerequisites

  Before you begin, make sure you have the following installed on your machine:

- Python 3.5 or higher
- Tweepy
- openai 



## Getting Started

1. Clone the repository to your local machine:

```terminal
git clone https://github.com/YOUR_USERNAME/SparrowAi.git -b template
```

2. Install the required packages:

```python
pip install -r requirements.txt
```

3. Generate your Twitter API keys and access tokens:
  - Go to https://developer.twitter.com/ and create a new app.
  - Click on the "Keys and Tokens" tab and generate your API keys and access tokens.
  - Also enable read and write permission.
  
4. Generate your OpenAI API key:
  - Go to https://beta.openai.com/ and create an account.
  - Navigate to the API keys section and generate a new API key.

4. Add your OpenAI and Twitter API keys to the `config.ini` file.

3. Run the `sparrowai.py` script to generate and post tweet.

```python
python sparrowai.py
```



## Customization

You can customize the prompts used to generate the tweet content by modifying the seeds list in the seeds.yaml file. This list contains a list of strings that will be passed to the davinci-03 model to generate the tweet content, and you can also modify the return statement of genPrompt function in the open.py file.

For example, if you want to generate a tweet about the weather, you could add the following prompt to the seeds list:
```yaml
seeds:
  - "about the weather today"
```

You can add as many prompts as you want to the Seeds list to generate a wide variety of tweets.



## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.



## Acknowledgments

- OpenAI for their davinci-03 model.
- Tweepy for their easy-to-use Twitter API library.
