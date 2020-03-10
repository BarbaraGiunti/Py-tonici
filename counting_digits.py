# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""

x = int( input( "Insert an integer: " ) )

# conta le cirfe di n
if x == 0 :
    count = 1
else :
    n = x
    count = 0
    while n != 0 and n != -1 :
        count = count + 1
        n = n // 10
print(x, " has ", count, " digits.")

# conta quanti 0 e 5 compaiono in n
if x == 0 :
    count = 1
else :
    n = x
    count = 0
    while n != 0 and n != -1  :
        digit = n % 10
        if digit == 0 or digit == 5 :
            count = count + 1
        n = n // 10
print(x, " contains ", count, " digits which are 0 or 5.")

# conta le cifre pari
if x == 0 :
    count = 1
else :
    n = x
    count = 0
    while n != 0 and n != -1  :
        digit = n % 10
        if digit % 2 == 0 :
            count += 1
        n = n // 10
print(x, " contains ", count, " even digits")