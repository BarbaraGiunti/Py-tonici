# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:39:57 2020

@author: Alberto Viscardi
"""

P = float( input( "Principal amount: " ) )
r = float( input( "Annual nomial interest rate: " ) )
n = int( input( "Number of times the interest is compounded per year: " ) )
t = int( input( "Number of years: " ) )

A = P * ( 1 + r / n ) ** ( n * t )
print( "The final amount of earning is: ", A )
