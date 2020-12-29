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
[String] -> Number
Gives average sentence count from a list of tweets
"""
def avg_sentences(texts):
  total = len(texts)
  sentence_count = 0

  for i in range(total):
    sentence_count += sentences(texts[i])

  return sentence_count / total

"""
String, Dictionary{word:frequency} -> Dictionary{word:frequency}
Case insensitive word frequency given a dictionary of word frequencies
"""
def count(text, counts):
  # lower case arg, split to words
  words = text.lower().split()

  # Store word frequencies in dictionary
  for w in words:
    if not w in counts.keys():
      counts[w] = 1
    else :
      counts[w] += 1

  return counts