# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:45:02 2018

@author: xxx
"""

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shiftedDict = {}
        for letter in string.ascii_lowercase:
            try:
                shiftedDict[letter] = string.ascii_lowercase[string.ascii_lowercase.index(letter)+shift]
            except IndexError:
                shiftedDict[letter] = string.ascii_lowercase[string.ascii_lowercase.index(letter)+shift-26]
        for sth in string.ascii_uppercase:
            try:
                shiftedDict[sth] = string.ascii_uppercase[string.ascii_uppercase.index(sth)+shift]
            except IndexError:
                shiftedDict[sth] = string.ascii_uppercase[string.ascii_uppercase.index(sth)+shift-26]
        return shiftedDict    

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        lookupDict = self.build_shift_dict(shift)
        self.message_text = list(self.message_text)
        for i in range (0,len(self.message_text)):
            try:
                self.message_text[i] = lookupDict[self.message_text[i]]
            except KeyError:
                pass
        self.message_text = ''.join(self.message_text)
        return self.message_text  