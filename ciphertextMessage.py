# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 00:30:26 2018

@author: xxx
"""

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text) 

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        
        '''
        
        
        
        #best tuple storing words to return in the end
        bestTupleTillNow = ()
        #tuple to compare with the best till now
        prollyBest = ()
        
        #loop looking for the best shift - using split()
        for s in range(0,25):
            #as long as there's sth in encrypted message
            for sth in self.message_text.split():
                #creating variable word, which is object type Message - for each
                # element
                word = Message(sth)
                #if 
                
                if is_word(self.valid_words, word.apply_shift(26 - s)):
                        prollyBest += (word.apply_shift(26-s),)
                        
                                        
            if len(prollyBest) >= len(bestTupleTillNow):
                bestTupleTillNow = prollyBest
                prollyBest = ()
                bestShift = 26 - s
                if bestShift == 26:
                    bestShift = 0
            else:
                prollyBest = ()
            
        return (bestShift,) + bestTupleTillNow