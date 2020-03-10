# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""

n = 1027371

""" 
while <CONDITION>:
    <STATEMENT>
"""

while n != 1:
    print(n, end=", ") # end="..." aggiunge dopo la stampa di n quello che c'è tra le virgolette
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = 3 * n
        n += 1 # l'operatore += prende il LHS e lo sostituisce con LHS + RHS
print(n, end=".\n") # \n indica un "a capo": il default senza \n fa comunque un a capo!