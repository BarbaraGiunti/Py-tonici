# Questo è un commento
"""
Questo è un altro commento: 
non essendo richiamato in una variabile 
rimane un commento ma questa scrittura può
essere intesa anche come una stringa in una 
assegnazione
"""

"""
CHAPTER 1
print("Hello, World!")
"""

"""
CHAPTER 2
message = 'And now for something completely different'
n=17
pi=3.1415926535897932
"""

"""
CHAPTER 3
"""

import math

def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day")
    
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
repeat_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)
    
phoebe = "Princess Consuelo Bananahammock"
print_twice(phoebe)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
    
line1 = "Un due tre "
line2 = "Sta lì!"

cat_twice(line1, line2)

result = print_twice(phoebe)

print(result)

def right_justify(s):
    print(" "*(70-len(s))+s)
    
right_justify("banana")


def do_twice(f):
    f()
    f()
    
def print_spam():
    print('spam')
    
do_twice(print_spam)

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_twice1(f, value):
    f(value)
    f(value)


do_twice1(print_twice, 'proooove')

def do_four1(f, value):
    do_twice1(f, value)
    do_twice1(f, value)
    
do_four1(right_justify, "opossum")


def row1():
    print("+", "-"*4, "+","-"*4, "+")
    
def row2():
    print("|", " "*4, "|"," "*4, "|")

def grid():
    row1()
    do_four(row2)
    row1()
    do_four(row2)
    row1()
    
grid()  


def row3():
    print("+", "-"*4, "+","-"*4, "+","-"*4, "+","-"*4, "+")
    
def row4():
    print("|", " "*4, "|"," "*4, "|"," "*4, "|"," "*4, "|")

def grid2():
    row3()
    do_four(row4)
    row3()
    do_four(row4)
    row3()
    do_four(row4)
    row3()
    do_four(row4)
    row3()
    
grid2()
