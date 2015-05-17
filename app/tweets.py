import re
import tweepy
import json
import nltk

with open('config/stopwords.txt', 'r') as stopwords_file:
    STOPWORDS = {line.strip() for line in stopwords_file}

with open('config/twitter.json', 'r') as twitter_config_file:
    _twitter_config = json.load(twitter_config_file)

CONSUMER_KEY = _twitter_config['consumer_key']
CONSUMER_SECRET = _twitter_config['consumer_secret']
ACCESS_TOKEN = _twitter_config['access_token']
ACCESS_TOKEN_SECRET = _twitter_config['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_tweets(screen_name):
    tweets = api.user_timeline(screen_name=screen_name,
                               include_rts=False,
                               count=200)

    return tweets

def tokenize_tweets(tweets):
    tokens = []
    for tweet in tweets:
        text = tweet.text.lower()
        text = re.sub(r"(?:\@|https?\://)\S+", '', text) # Remove URLs
        for token in nltk.tokenize.word_tokenize(text):
            if 3 < len(token) and token not in STOPWORDS:
                tokens.append(token)

    return tokens

def top_tokens(tokens, n=20):
    freq_dist = nltk.FreqDist(tokens)

    return freq_dist.most_common(n)
    
