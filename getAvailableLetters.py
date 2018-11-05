# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:27:11 2018

@author: xxx
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    availableLetters = string.ascii_lowercase
    
    for letter in lettersGuessed:
       if letter in availableLetters:
           availableLetters = availableLetters.replace(letter, "")                 
    return availableLetters
