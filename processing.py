# Performs sentiment analysis on a string
from textblob import TextBlob as tb

"""
String -> Sentiment Scores(Polarity, Subjectivity)
-1 = negative
1 = positive

0 = objective
1 = subjective
"""
def sentiment(text):
  return tb(text).sentiment

"""
String -> Int
Counts sentences
"""
def sentences(text):
  return len(tb(text).sentences)

"""
String -> Dictionary{word:frequency}
Case insensitive word frequency
"""
def count(text):
  # lower case arg, split to words
  words = text.lower().split()

  # Store word frequencies in dictionary
  counts = {}
  for w in words:
    if not w in counts.keys():
      counts[w] = 1
    else :
      counts[w] += 1

  return counts