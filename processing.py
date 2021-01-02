"""
Implements all processing functions
"""

"""-----------------------------------------------------------------------------
String, Dictionary{word:frequency} -> Dictionary{word:frequency}
Case insensitive word frequency given a dictionary of word frequencies
"""
def count(tweets):
  total = 0        # total number of words
  popular = []     # most frequent words
  counts = {}      # number of word occurances
  
  # Use all tweets
  for tweet in all tweet:

    total += len(tweet)
    message = tweet.lower().split()

    # Use all words
    for word in message:
        counts[word] = counts[word] + 1 if word in counts.keys() else 0

  # Get list of top frequent words   

"""
sum of product of of tweet sentiments * frequency 
"""