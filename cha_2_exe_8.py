# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:47:31 2020

@author: Alberto Viscardi
"""

T = int( input( "What hour is it? " ) )
S = int( input( "How many hours do you want to sleep? " ) )
F = ( T + S ) % 24

print( "You will wake up at ", F )