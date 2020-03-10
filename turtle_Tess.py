# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""
new_color = input("Please enter the initial background color: ")

import turtle
window = turtle.Screen()
window.bgcolor(new_color) # Set the window background color
window.title("Hello, Tess!") # Set the window title

tess = turtle.Turtle()
tess.color("blue") # Tell tess to change her color
tess.pensize(3) # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

new_color = input("If you want, insert a new color for the background: ")
window.bgcolor(new_color)

window.mainloop()