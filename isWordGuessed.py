# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:25:18 2018

@author: xxx
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
  
    secretWord2 = [] 
    for j in secretWord:
        secretWord2.append('')
     
    for index in range(len(lettersGuessed)):
        for letter in range(len(secretWord)):
            if lettersGuessed[index] == secretWord[letter]:
                secretWord2[letter] = secretWord[letter]
    secretWord2 = ''.join(secretWord2)    
    if secretWord2 == secretWord:
        return True
    else:
        return False