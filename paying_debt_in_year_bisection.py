# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:20:59 2018

@author: xxx
"""
#
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
#
#Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem

month = 1
copyBalance = balance
monthlyInterestRate = annualInterestRate/12
monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound = (balance*(1+monthlyInterestRate)**12)/12.0
monthlyPaymentRate = (monthlyPaymentLowerBound+monthlyPaymentUpperBound)/2.0

while copyBalance > 0:
    while month <= 12:
        copyBalance -= monthlyPaymentRate
        copyBalance = round(copyBalance + annualInterestRate/12.0 * copyBalance, 3)
        month += 1
    if copyBalance > 0:
        month = 1
        copyBalance = balance
        monthlyPaymentLowerBound = monthlyPaymentRate
        monthlyPaymentRate = (monthlyPaymentLowerBound+monthlyPaymentUpperBound)/2.0
    elif copyBalance < 0:
        month = 1
        copyBalance = balance
        monthlyPaymentUpperBound = monthlyPaymentRate
        monthlyPaymentRate = (monthlyPaymentLowerBound+monthlyPaymentUpperBound)/2.0
    else:
        break


print ("Lowest Payment: " + str(round(monthlyPaymentRate,2)))    