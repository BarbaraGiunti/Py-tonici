# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:29:21 2020

@author: utente


def recursion_depth(number):
    print("recursion depth number", number)
    try:
        recursion_depth(number+1)
    except:
        print("I cannot go any deeper into this wormhole")
        
recursion_depth(0)
"""

def readposint():
    posint = input("Please enter a positive integer")
    
    if type(posint) != int:
        error = ValueError("{0} is not an integer".format(posint))
        raise error
    elif posint < 0:
        error = ValueError("{0} is negative".format(posint))
        raise error

    return posint