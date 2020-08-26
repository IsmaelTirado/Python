#!/usr/bin/env python3

import sys

def match_words(words):
  ctr = 0

  for word in words:
    #char_index = len(word) -1
    if len(word) > 1 and word[0] == word[len(word)-1]:
      ctr += 1
  return ctr
words = (sys.argv)
print(match_words(words))

