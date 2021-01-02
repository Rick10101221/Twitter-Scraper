"""
Retrieves a twitter user's most recent tweets and retweets on their Twitter
timeline based off of the number of tweets they want to retrieve, the user's
screen name, and whether or not they want to include retweets
"""
import re
from html import unescape
import tweepy
from api_key import consumer_key
from api_key import consumer_secret

RT_HEADER = 'RT @'      # Indicates whether or not tweet is a retweet
RT_HEADER_LEN = 4       # Length of RETWEET_HEADER
RT_HEADER_OFFSET = 2    # Offset between RETWEET_HEADER and retweet text
"""
Unicode blocks of emojis used to find and filter emojis from tweets

References: https://gist.github.com/Alex-Just/e86110836f3f93fe7932290526529cd1#gistcomment-3208085
"""
EMOJI_PATTERN = re.compile(
        "(["
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "])"
)

# Tweepy auth
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

"""
tweet_list: List of tweets to filter through

Returns a new list of tweets without retweets from an unfiltered tweets list
"""
def remove_rt(tweet_list):
    #new list to store all tweets that aren't retweets
    new_list = []
    # Iterates through most recent tweets and retweets in user's timeline
    for tweet in tweet_list:
        # If tweet is a not a retweet then include it. Otherwise, skip it.
        if RT_HEADER != (tweet.full_text[:RT_HEADER_LEN]):
            new_list.append(tweet.full_text)
        else:
            continue
    return new_list

"""
tweet_list: List of tweets to filter through

Returns a new list of tweets inlcuding retweets that has been processed
"""
def include_rt(tweet_list):
    #list to store all tweets and retweets without their header
    new_list = []
    for tweet in tweet_list:
        """
        If tweet is a not a retweet then include it. Otherwise, process 
        the tweet before including it
        """
        if RT_HEADER != (tweet.full_text[:RT_HEADER_LEN]):
            new_list.append(tweet.full_text)
        else:
            start_index = tweet.full_text.find(':') + RT_HEADER_OFFSET
            new_list.append(tweet.full_text[start_index:])
    return new_list

"""
screen_name:    screen name of user to collect tweets from
tweet_num:      number of most recent tweets to collect
remove_rt:      describes whether or not to filter out retweets from the tweets
                collected

Retrieves a specific amount of the most recent tweets from a specific user and 
decides whether or not to filter out their retweets.
Returns a list of the tweet's text.
"""
def get_tweets(screen_name, tweet_num, allowing_rt):
    # List of specified number of recent tweets
    timeline = tweepy.Cursor(
            api.user_timeline,
            id=screen_name,
            tweet_mode='extended').items(tweet_num)

    # Checks whether or not to include retweets
    if not allowing_rt:
        # Returns list of recent tweets with retweets filtered out
        return remove_rt(timeline)
    else:
        # Returns list of recent tweets with retweets filtered out
        return include_rt(timeline)

"""
tweet_list: List of tweets that needs to be cleaned

Returns a new list of tweets that does not include any image/video links, any 
@ reply flags, HTML entities, emojis, and any # in tags
"""
def clean_tweets(tweet_list):
    #new list to return cleaned up tweets
    new_list = []
    for tweet in tweet_list:
        temp = re.sub(r'@\w+', '', tweet)    # Removes reply flags
        temp = re.sub(r'https://t\.co/\w+', '', temp)    # Removes links
        temp = unescape(temp)    # Unescapes HTML entities
        temp = EMOJI_PATTERN.sub(r'', temp)    # Removes emojis
        temp = temp.replace('#', '')    # Removes # for tags
        cleaned_tweet = temp.strip()    #Strips any leftover whitespace
        # Appends tweet if it still has text content inside to analyze
        if len(cleaned_tweet) > 0:
            new_list.append(cleaned_tweet)
    return new_list

"""
User input for testing

screen_name = input('Enter the screen name you want to collect tweets from: ')
tweet_num = int(input('\nEnter the number of tweets you want from them: '))
allowing_rt = int(input('\nEnter 1 to include retweets. Otherwise, enter 0: '))
"""

"""
Call get_tweets to store list of tweets

tweets = get_tweets(screen_name, tweet_num, allowing_rt)
final_tweets = clean_tweets(tweets)
"""

"""
Prints all valid tweets retrieved and their length for testing

print(*final_tweets, sep = '\n\n----------------------------------------------\n\n')
print(f'{len(final_tweets)} valid tweets returned')
"""