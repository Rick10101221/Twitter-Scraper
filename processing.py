"""
Implements all processing functions

Useful things to import:
- avg_sentiment  | sentiment analysis
- avg_sentences  | average sentence count 
- count          | word frequencies
"""
from textblob import TextBlob as tb

"""-----------------------------------------------------------------------------
String -> Sentiment Scores(Polarity, Subjectivity)
-1 = negative
1 = positive

0 = objective
1 = subjective
"""
def sentiment(text):
  return tb(text).sentiment

"""
[String] -> Sentiment Scores(Polarity, Subjectivity)
Gives an average sentiment value for list of tweets
"""
def avg_sentiments(texts):
  total = len(texts)
  polarity_total, subjectivity_total = 0, 0
  
  # Sums up all the polarity/subjectivity values
  for i in range(total):
    sentiments = sentiment(texts[i])
    polarity_total += sentiments[0]
    subjectivity_total += sentiments[1]
  
  return (polarity_total / total, subjectivity_total / total)

"""-----------------------------------------------------------------------------
String -> Int
Counts sentences
"""
def sentences(text):
  return len(tb(text).sentences)


"""-----------------------------------------------------------------------------
[String] -> Number
Gives average sentence count from a list of tweets
"""
def avg_sentences(texts):
  total = len(texts)
  sentence_count = 0

  # Sums up all sentences in tweets
  for i in range(total):
    sentence_count += sentences(texts[i])

  return sentence_count / total

"""-----------------------------------------------------------------------------
String, Dictionary{word:frequency} -> Dictionary{word:frequency}
Case insensitive word frequency given a dictionary of word frequencies
"""
def count(text, counts):
  words = text.lower().split()

  # Update word frequencies to dictionary
  for w in words:
    if not w in counts.keys():
      counts[w] = 1
    else :
      counts[w] += 1

  return counts