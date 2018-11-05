# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:29:02 2018

@author: xxx
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed =[]
    mistakesMade = 0
    print ("Welcome to the game Hangman!")
    print (" I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("-------------")
    
    availableLetters = getAvailableLetters(lettersGuessed)
    while mistakesMade < 8:
        print("You have " + str(8 - mistakesMade) + " guesses left.")
        print("Available letters: " + availableLetters)
        guess = input("Please guess a letter: " )
        guess = guess.lower()
        lettersGuessed.append(guess)
        if guess in availableLetters:
            if guess in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed) )
            else:
                mistakesMade += 1
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        
        availableLetters = getAvailableLetters(lettersGuessed)
        print("-------------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
    if mistakesMade == 8:
        print ("Sorry, you ran out of guesses. The word was " + secretWord + ".")