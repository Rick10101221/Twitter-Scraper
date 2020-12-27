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
