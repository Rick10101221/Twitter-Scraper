# Counts word frequency of string

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