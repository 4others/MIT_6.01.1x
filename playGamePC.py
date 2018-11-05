# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:47:01 2018

@author: xxx
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #initiative value
    hand = None
    letter = None

    #as long as the game goes
    while letter != 'e':
        letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if letter != 'e' and letter != 'r' and letter != 'n':
                print("Invalid command.")
                
        #if there was no hand before
        while letter == 'r' and hand is None:
            print("You have not played a hand yet. Please play a new hand first!")
            letter = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            
            
        if letter == 'n' or letter == 'r':
            whoPlays = input("Enter u to have yourself play, c to have the computer play: ")
            while whoPlays != 'c' and whoPlays != 'u':
                print("Invalid command.")
                whoPlays = input("Enter u to have yourself play, c to have the computer play: ")
            if whoPlays == 'c' and letter == 'n':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand,wordList, HAND_SIZE)
            elif whoPlays == 'u' and letter =='n':
                hand = dealHand(HAND_SIZE)
                playHand(hand,wordList, HAND_SIZE)
            elif whoPlays == 'c' and letter == 'r':
                compPlayHand(hand,wordList, HAND_SIZE)
            else:
                playHand(hand,wordList, HAND_SIZE)
