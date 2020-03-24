# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:15:49 2020

@author: utente
"""

"""
def find2(haystack, needle, start):
    for index, letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
        
    return -1

print(find2("banana", "n", 2))


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

        
def count_letters(word, t_letter):
    count = 0
    for letter in word:
        if letter == t_letter:
            count += 1
            
    return(count)
    
def count_letters_f(word, t_letter):
    count = 0
    i = 1
    while i < len(word):
        #print(i, word.find(t_letter, i))
        a = word.find(t_letter, i)
        if a > -1:
            count += 1
            i += a
        else: 
            break
    if word[0] == t_letter:
        count += 1
            
    return(count)   
    
print(count_letters("banana", "n"))  
print(count_letters_f("banana", "b"))  


def reverse(string):
    a = ""
    for idx in range(1, len(string)+1):
        a += string[-idx]
        
    return a

print(reverse("good"))

def mirror(string):
    a = string
    for idx in range(1, len(string)+1):
        a += string[-idx]
        
    return a
    
print(mirror("good"))   
    
  
    
def remove_letter(letter, string):
    s = ""
    for x in string:
        if x != letter:
            s += x
            
    return s

print(remove_letter("a", "apple"))  
print(remove_letter("a", "banana"))  
print(remove_letter("z", "ornitorinco"))   


def is_palindrome(string):
    if string == reverse(string):
        return True
    else:
        return False

print(is_palindrome("abba"))
print(is_palindrome("tenet"))
print(is_palindrome("sator"))
""" 

def count_letters(tuple_arg):
    count = 0
    for letter in tuple_arg[0]:
        if letter == tuple_arg[1]:
            count += 1
            
    return(count)

print(count_letters(("banana", "n"))) 

    