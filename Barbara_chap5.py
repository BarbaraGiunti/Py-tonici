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
 

def count_letters(tuple_arg):
    count = 0
    for letter in tuple_arg[0]:
        if letter == tuple_arg[1]:
            count += 1
            
    return(count)

print(count_letters(("banana", "n"))) 


import string

text = input("Insert your favorite text into triple quote")


def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    
    return phrase_sans_punct

split_text = remove_punctuation(text).split()

def count_e(split_text):
    count = 0
    for word in split_text:
        if "e" in word:
            count += 1
            
    return count

e_text = count_e(split_text)

percent = 100*e_text/len(split_text)

print("Your text contains ", len(split_text), "words, of which ", e_text, "(",percent,"%) contain an 'e'.")


def add_vectors(v1,v2):
    v = []
    if len(v1)==len(v2):
        for i in range(len(v1)):
            v += [v1[i] + v2[i]]
    else:
        print("I cannot add apples and pears!")
    
    return v

v1 = [1,2,1]
v2 = [1,4,3]

v = add_vectors(v1,v2)
print(v)


def scalar_mult(s,v):
    v1 = []
    for i in range(len(v)):
            v1 += [s*v[i]]
 
    return v1

print(scalar_mult(5,[1,2]))
print(scalar_mult(3,[1,0,-1]))
print(scalar_mult(7,[3,0,5,11,2]))



def dot_product(v1,v2):
    result = 0
    if len(v1)==len(v2):
        for i in range(len(v1)):
            result += v1[i] * v2[i]
    else:
        print("I cannot add apples and pears!")
    
    return result

print(dot_product([1,1],[1,1]))
print(dot_product([1,2],[1,4]))
print(dot_product([1,2,1],[1,4,3]))

"""

def occurrency(string):
    string = string.lower()

    letter_counts = {}
    for letter in string:
        if letter != " ":
            letter_counts[letter] =  letter_counts.get(letter, 0) + 1
        
    
    letter_items = list(letter_counts.items())
    letter_items.sort()
    
    print(letter_items)


string = "ThiS is String with Upper and lower case Letters"

occurrency(string)















































    