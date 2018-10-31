# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:46:08 2018

@author: xxx
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    hand = None
    letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
    while letter != 'e':
        if letter == 'r':
            if hand is None:
                print("You have not played a hand yet. Please play a new hand first!")
                letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            else:
                playHand(hand,wordList, HAND_SIZE)
                letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif letter != 'e' and letter != 'r' and letter != 'n':
                print("Invalid command.")
                letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        else:
            hand = dealHand(HAND_SIZE)
            playHand(hand,wordList, HAND_SIZE)
            letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
       

