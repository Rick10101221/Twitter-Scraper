import tweepy
from api_key import consumer_key
from api_key import consumer_secret

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

def get_tweets(tweet_num, twitter_handle, remove_rt):
    tweets = []
    count = tweet_num
    if remove_rt:
        for tweet in tweepy.Cursor(api.user_timeline, id=twitter_handle).items(count):
            if 'RT @' != tweet.text[:4]:
                tweets.append(tweet.text)
            else:
                continue
        return tweets
    else:
        for tweet in tweepy.Cursor(api.user_timeline, id=twitter_handle).items(count):
            tweets.append(tweet.text)
        return tweets


input_handle = input('Enter the screen name of the twitter account you want to collect tweets for: ')
input_number = int(input('\nEnter the number of tweets you want from them (minimum=0 maximum=350): '))
input_remove_rt = int(input('\nEnter 1 to not include retweets. Otherwise, enter 0: '))

tweets = get_tweets(input_number, input_handle, input_remove_rt)

print(*tweets, sep = "\n\n")
print(len(tweets))
