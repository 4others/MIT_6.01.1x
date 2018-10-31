# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:10:10 2018

@author: xxx
"""

#Assume s is a string of lower case characters.
#
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#
#Number of times bob occurs is: 2

bobby = 0
i = 0
while i <= (len(s)-3):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        bobby += 1
    i += 1    
print ("Number of times bob occurs: " + str(bobby))