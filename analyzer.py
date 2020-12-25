# Performs sentiment analysis on a string
from textblob import TextBlob as tb

"""
String -> Sentiment Scores
"""
def analyze(text):
  blob = tb(text)
  return blob.sentiment


"""
.sentiment tuple
(polarity, subjectivity)

-1 = negative
1 = positive

0 = objective
1 = subjective
"""