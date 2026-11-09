def count_vowels(x):
  '''
  str -> int

  counts the number of vowels in a given character string.

  >>> count_vowels("my name is Earl")
  5
  '''
  return sum(1 for char in x.lower() if char in 'aeiou')
