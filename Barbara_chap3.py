# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:56:44 2020

@author: utente
"""

"""
import turtle


col_screen = input("What color screen do you want? ")
greetings = input("Greet your turtle!")


for friend in ["Banana", "Opossum", "Birdino", "Patata"]:
    invite = "Hi, " + friend + ". Plese come to my party!"
    print(invite)


window = turtle.Screen()
window.bgcolor("cornflower blue")
window.title("Hi tutline!")

#create tess with some attribute
tess = turtle.Turtle()
tess.color("blue")
#tess.pensize(5)
tess.shape("turtle")

tess.penup()
size = 15

for _ in range(30):
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)


#create alex
alex = turtle.Turtle()

#tess draws equilateral triangle
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

#alex draws a square

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

for i in range(4):
    alex.forward(50)
    alex.left(90)

colors = ["yellow", "red", "purple", "blue"]
for color in colors:
    alex.color(color)
    alex.forward(50)
    alex.left(90)


alex.penup
alex.forward(100)
alex.pendown()

alex.shape("turtle")

alex.speed(1)


window.mainloop()

turtle.done()
turtle.bye() 


if True:
    pass
else:
    pass
    
    
total = 0
while True:
    response = input("Enter the next number - leave blank to end ")
    if response == " ":
        break
    total += int(response)
    
print("The total of the numbers you entered is ", total)

while True:
    #play_the_game_once()
    response = input("Play again? (yes or no)")
    if response != "yes":
        break
print("Goodbye!")
"""

#Exercise 1
"""
#number = int(input("Tell me the day number"))

def week_day(number):
    if number < 0 or number > 7:
        print("That's not a day number!")
    elif number == 0:
        print("Sunday")
    elif number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    else:
        print("Saturday")

#week_day(number)

def day():
    s = int(input("Tell me the starting day number "))
    n = int(input("Tell me how long is your stay "))
    number = (s + n) % 7
    week_day(number)
    
day()
"""

#Exercise 6
"""
def grade(mark):
    if mark >= 75:
        print("First")
    elif 70 <= mark < 75:
        print("Upper second")
    elif 60 <= mark < 70:
        print("Second")
    elif 50 <= mark < 60:
        print("Third")
    elif 45 <= mark < 50:
        print("F1 Supp")
    elif 40 <= mark < 45:
        print("F2")
    else:
        print("F3")

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for n in numbers:
    grade(n)
"""

#Exercise 7
"""
def hypotenuse(c1, c2):
    h = (c1**2 + c2**2)**0.5
    return h

print(hypotenuse(4,3))

#Exercise 8-9

def is_t_rectagle(a,b,c):
    threshold = 1e-7
    if a < b and c < b:
        h = hypotenuse(a,c)
        if abs(h-b) < threshold:
            return(True)
        else:
            return(False)  
    elif b < a and c < a:
        h = hypotenuse(b,c)
        if abs(h-a) < threshold:
            return(True)
        else:
            return(False)
    elif b < c and a < c:
        h = hypotenuse(b,a)
        if abs(h-c) < threshold:
            return(True)
        else:
            return(False)

test1 = is_t_rectagle(3,4,5)
print(test1)

test2 = is_t_rectagle(3,4,6)
print(test2)
"""
#Exercise 11 (or 1 pag 60)
"""
for _ in range(1000):
    print("We like Python's turtle!")      
    #that was exciting -.-
"""  
#Exercise 12 (or 2 pag 60)
"""
for month in ["January", "February", "Mars", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    print("One of the months of the year is " + month)
"""

#Exercise 14 (or 4 pag 60)
"""
numbers = [12,10,32,3,66,17,42,99,20]

total_sum = 0
total_mul = 1

for x in numbers:
    print(x, x**0.5, "\n")
    total_sum += x
    total_mul = total_mul*x

print(total_sum, "\t", total_mul)
"""

#Exercise wtf_I_guess_we_dont_use_numbers pag 61
"""
def play_list_n(numbers):
    count = 0
    total_sum_even = 0
    for n in numbers:
        if n % 2 == 1:
            count += 1
        else:
            total_sum_even += n 
    return(count, total_sum_even)       
    

numbers = [12,10,32,3,66,17,42,99,20]

o = play_list_n(numbers)
print(o)


def sum_neg(numbers):
    total = 0
    for n in numbers:
        if n<0:
            total += n
    return(total)
            
numbers1 = [12,-10,32,3,66,-17,42,99,-20]
    
x = sum_neg(numbers1)
print(x)


def len_5(words):
    count = 0
    for w in words:
        if len(w) == 5:
            count += 1
    return(count)

words = ["banana", "penguin", "lacca", "crepa", "ecco!"]

x = len_5(words)
print(x)

def sum_up(numbers):
    total = 0
    for n in numbers:
        if n%2 == 0:
            break
        else:
            total += n
    return(total)

numbers = [11,15,33,3,17,99,23]

x = sum_up(numbers)
print(x)

def is_prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print(False)
            break
    else:
        print(True)
        
x = 9
is_prime(x)

def even_digit(n):
    count = 0
    while n > 0:
        x = n%10
        if x%2 == 0:
            count += 1 
        n = n//10
    print(count)
        
even_digit(1023452)


def sum_square(numbers):
    total = 0
    for n in numbers:
        total += n**2
    print(total)

numbers = [2,5,4,1]
sum_square(numbers)
"""