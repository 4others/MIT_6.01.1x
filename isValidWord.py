# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:44:01 2018

@author: xxx
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if not word in wordList:
        return False
    count = 0
    handCopy = hand.copy()
    for letter in word:
        if handCopy.get(letter,0) != 0:
            count += 1
            handCopy[letter] = handCopy.get(letter,0) - 1
    if len(word) == count:
        return True
    return False
