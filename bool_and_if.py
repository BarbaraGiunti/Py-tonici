# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""

# I valori di verità in python sono "True" e "False" (case sensitive!)
# Operazioni di comparazione che restituiscono elementi di tipo "bool" sono:
# ==, !=, <, >, <=, >=
# Operatori logici tra "bool" sono "and", "or" e "not" utilizzati in modo abbastanza naturale

x = int( input("Insert an integer: ") )

"""
if <BOOLEAN EXPRESSION>:
    <STATEMENTS_1> # Executed if condition evaluates to True
else:
    <STATEMENTS_2> # Executed if condition evaluates to False
"""
# l'else si può chiaramente omettere
# la keyword "pass" fa sì che quel ramo dell'if non faccia niente
# si possono concatenare più if usando "else if" o "elif"

import math

if x < 0:
    print("The negative number ", x, " is not valid here.")
    x = 42
    print("I've decided to use the number 42 instead.")

if x % 2 == 0:
    print(x, " is even.")
    print("Did you know that 2 is the only even number that is prime?")
else:
    print(x, " is odd.")
    print("Did you know that multiplying two odd numbers " +
        "always gives an odd result?")

print("The square root of ", x, "is", math.sqrt(x))