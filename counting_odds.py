 # -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""

numbers = [ 1, 7, 9 ] #[10, 5, 24, 8, 6]

print("There is at least an odd number: ", end=" ")
for number in numbers:
    if number % 2 == 1:
        print(True)
        break
else: # questo else è legato al for e viene attivato se il for si è concluso senza bisogno di break
    print(False)

print("There are only odd numbers: ", end=" ")
for number in numbers:
    if number % 2 == 0:
        print(False)
        break
else: 
    print(True)

print("There are at least three odd numbers: ", end=" ")
count = 0
for number in numbers:
    if number % 2 == 1:
        count += 1
    if count == 3:
        print(True)
        break
else: 
    print(False)