"""
Retrieves a twitter user's most recent tweets and retweets on their Twitter
timeline based off of the number of tweets they want to retrieve, the user's
screen name, and whether or not they want to include retweets
"""

import tweepy
from api_key import consumer_key
from api_key import consumer_secret

# Tweepy auth
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

"""
tweet_num:      number of most recent tweets to collect
twitter_handle: screen name of user to collect tweets from
remove_rt:      describes whether or not to filter out retweets from the tweets
                collected

Retrieves a specific amount of the most recent tweets from a specific user and 
decides whether or not to filter out their retweets.
Returns a list of the tweet's text.
"""
def get_tweets(tweet_num, twitter_handle, remove_rt):
    RT_HEADER = 'RT @'      # Indicates whether or not tweet is a retweet
    RT_HEADER_LEN = 4       # Length of RETWEET_HEADER
    RT_HEADER_OFFSET = 2    # Offset between RETWEET_HEADER and retweet text

    recent_tweets = \
        tweepy.Cursor(api.user_timeline, id=twitter_handle).items(tweet_num)
                            # List of specified number of recent tweets
    tweets = []             # List of tweets to return

    # Checks whether or not to include retweets
    if remove_rt:
        # Iterates through most recent tweets and retweets in user's timeline
        for tweet in recent_tweets:
            # If tweet is a not a retweet then include it. Otherwise, skip it.
            if RT_HEADER != (tweet.text[:RT_HEADER_LEN]):
                tweets.append(tweet.text)
            else:
                continue
        # Returns list of recent tweets with retweets filtered out
        return tweets
    else:
        for tweet in recent_tweets:
            """
            If tweet is a not a retweet then include it. Otherwise, process 
            the tweet before including it
            """
            if RT_HEADER != (tweet.text[:RT_HEADER_LEN]):
                tweets.append(tweet.text)
            else:
                start_index = tweet.text.find(':') + RT_HEADER_OFFSET
                tweets.append(tweet.text[start_index:])
        # Returns list of recent tweets with retweets filtered out
        return tweets

"""
User input for testing

input_handle = input('Enter the screen name you want to collect tweets from: ')
input_number = int(input('\nEnter the number of tweets you want from them: '))
input_remove_rt = int(input('\nEnter 1 to remove retweets. Otherwise, enter 0: '))
"""

# Call get_tweets to store list of tweets
tweets = get_tweets(input_number, input_handle, input_remove_rt)

"""
Prints all tweets retrieved and their length for testing

print(*tweets, sep = '\n\n')
print(len(tweets))
"""