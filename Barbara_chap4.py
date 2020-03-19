# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:15:53 2020

@author: utente
"""

import turtle

"""
def draw_square(animal,size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

window = turtle.Screen()
window.bgcolor("cornflower blue")
window.title("Alex meets a function")

alex = turtle.Turtle()
draw_square(alex, 50)


def draw_multicolor_square(animal, size):
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)
        
window = turtle.Screen()
window.bgcolor("cornflower blue")

tess = turtle.Turtle()
tess.pensize(3)

size = 20

for _ in range(15):
    draw_multicolor_square(tess, size)
    size += 10
    tess.forward(10)
    tess.right(18)


def draw_rectangle(animal, width, height):
    for _ in range(2):
        animal.forward(width)
        animal.left(90)
        animal.forward(height)
        animal.left(90)

def draw_square(animal, size):
    draw_rectangle(animal, size, size)




def final_amount(p, r, n, t):
    
    a = p * (1 + r/n) ** (n*t)
    return a

toInvest = float(input("How much do you want to invest? "))

fnl = final_amount(toInvest, 0.08, 12, 5)
print("At the end of the period, you'll have ", fnl)



def make_window(color, title):
    
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color, size):
    
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal



tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)


def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

def draw_multi_squares(animal, size, n):
    
    for _ in range(n):
        draw_square(animal, size)
        animal.penup()
        animal.forward(size * 2)
        animal.pendown()
        
def draw_inner_squares(animal, size, n):
    
    for _ in range(n):
        draw_square(animal, size)
        size += 20
        animal.penup()
        animal.right(90)
        animal.forward(10)
        animal.right(90)
        animal.forward(10)
        animal.left(180)
        animal.pendown()
        
def draw_poly(t, n, sz):
    
    for _ in range(n):
        t.forward(sz)
        t.left(int(360/n))

def draw_pretty_pattern(animal, size, n):
    
    for _ in range(n):
        draw_square(animal, size)
        animal.left(int(360/n))
        
def draw_spiral(animal, in_size, s, shift_angle, n):
    
    animal.right(90)
    
    for _ in range(n):
        animal.forward(in_size)
        in_size += s
        animal.right(90 + shift_angle)
        
def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)
       
wn = make_window("cornflower blue", "Turtline squares")

tess = make_turtle("hotpink", 2)

#draw_multi_squares(tess, 20, 5)

#draw_inner_squares(tess, 20, 5)

#draw_poly(tess, 8, 50)

#draw_pretty_pattern(tess, 50, 20)

#draw_spiral(tess, 3, 1, 2, 150)

draw_equitriangle(tess, 20)

wn.mainloop()

turtle.done()
turtle.bye() 


def sum_to(n):
    
    s = 0
    
    for x in range(1, n+1):
        s += x
    return(s)
    
sum_n = sum_to(10)
print(sum_n)


def turn_clockwise(comp_point):
    
    if comp_point == "N":
        return "E"
    elif comp_point == "E":
        return "S"
    elif comp_point == "S":
        return "W"
    elif comp_point == "W":
        return "N"
    else:
        return

card = input("Which compass point do you want to turn? ")

a = turn_clockwise(card)
print(a)


def days_in_month(month):
    
    if month in ["January", "March", "May", "July", "August", "October", "December"]:
        return 31
    elif month in ["April", "June", "September", "November"]:
        return 30
    elif month == "February":
        return 28
    else: 
        return 

month = input("Which month point do you want to test? ")

a = days_in_month(month)
print(a)


def to_secs(h, m, s):
    
    return(int(h)*3600+int(m)*60+int(s))

#print(to_secs(2,30,10))
#print(to_secs(2,0,0))
#print(to_secs(0,2,0))
#print(to_secs(0,0,42))
#print(to_secs(0,-10,10))

print(to_secs(2.5,30,10.71))
print(to_secs(2.433,0,0))


def hours_in(secs):
    return(secs//3600)
    
def minutes_in(secs):
    h = hours_in(secs)
    secs = secs - 3600*h
    return(secs//60)

def seconds_in(secs):
    h = hours_in(secs)
    m = minutes_in(secs)
    return(secs - 3600*h - 60*m)

print(hours_in(9010))  
print(minutes_in(9010))
print(seconds_in(9010))


def slope(x1,y1,x2,y2):
    m = float((y1-y2)/(x1-x2))
    return m

print(slope(5,3,4,2))
print(slope(1,2,3,2))
print(slope(1,2,3,3))
print(slope(2,4,1,2))
"""










