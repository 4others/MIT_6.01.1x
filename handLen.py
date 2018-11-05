# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:44:41 2018

@author: xxx
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    for sth in hand.values():
        handLen += sth
    return handLen    
