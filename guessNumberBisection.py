# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:37:51 2018

@author: xxx
"""

print("Please, think of a number between 0 and 100:")
start = 0
end = 100
shot = (start+end)/2
print ("Is your secret number " + str(int(shot)) + "?")
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "  ) 
while guess != 'c' and guess != 'h' and guess != 'l':
    print ("Sorry, I did not understand your input.")
    print ("Is your secret number " + str(int(shot)) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "  ) 
while guess != 'c':
    if guess == 'h':
        end = int(shot)
        shot = (start+end)/2 
        print ("Is your secret number " + str(int(shot)) + "?")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        while guess != 'c' and guess != 'h' and guess != 'l':
            print ("Sorry, I did not understand your input.")
            print ("Is your secret number " + str(int(shot)) + "?")
            guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "  )
        
    elif guess == 'l':
        start = int(shot)
        shot = (start+end)/2
        print ("Is your secret number " + str(int(shot)) + "?")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        while guess != 'c' and guess != 'h' and guess != 'l':
            print ("Sorry, I did not understand your input.")
            print ("Is your secret number " + str(int(shot)) + "?")
            guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "  )
print("Game over. Your secret number was: " + str(int(shot)) +"!") 