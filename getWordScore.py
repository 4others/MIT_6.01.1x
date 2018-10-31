# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:30:11 2018

@author: xxx
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    if len(word) == 0:
        return 0
    else:
        altogether = 0
        freq = {}
        for x in word:
            freq[x] = freq.get(x,0) + 1
    
        for key in freq:
            altogether += freq[key]*SCRABBLE_LETTER_VALUES[key]
        altogether *= len(word)
        if len(word) == n:
            altogether += 50
        return altogether  
