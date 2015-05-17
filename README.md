# Top terms for a Twitter user

This single page app takes a Twitter screen name and returns their
most recently tweeted words.  The idea was to put this into a
d3-powered word cloud but I was having a hard time getting d3 and
React to play nicely.

## Installation

Run `script/install.sh`.  This downloads the files `nltk` requires to
tokenize its input.

Add a static JSON file at `app/config/twitter.json' with Twitter app
credentials in the following format:

```
{
    "consumer_key": "<CONSUMER KEY>",
    "consumer_secret": "<CONSUMER SECRET>",
    "access_token": "<ACCESS TOKEN>",
    "access_token_secret": "<ACCESS TOKEN SECRET>"
}
```

## Running

```
cd app
python main.py
```
