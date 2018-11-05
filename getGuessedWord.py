# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:26:16 2018

@author: xxx
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretWord2 = []
    for j in secretWord:
        secretWord2.append('_')
    for index in range(len(lettersGuessed)):
        for letter in range(len(secretWord)):
            if lettersGuessed[index] == secretWord[letter]:
                secretWord2[letter] = secretWord[letter]
    return(' '.join(secretWord2))            
