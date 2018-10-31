# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:13:13 2018

@author: xxx
"""
#
#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
#Longest substring in alphabetical order is: abc

i = 0
first = s[0]
second = s[0]
while i <=(len(s)-2):
    if s[i] <= s[i+1]:
        first += s[i+1]
        if len(first) > len(second):
            second = first
        i += 1    
    else:
        first = s[i+1]
        i += 1
print ("Longest substring in alphabetical order is: " + second) 