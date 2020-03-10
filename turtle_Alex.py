# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:32:47 2020

@author: Alberto Viscardi
"""

import turtle # Allows us to use turtles
window = turtle.Screen() # Creates a playground for turtles
alex = turtle.Turtle() # Create a turtle, assign to alex

alex.forward(50) # Tell alex to move forward by 50 units
alex.left(90) # Tell alex to turn by 90 degrees
alex.forward(30) # Complete the second side of a rectangle

window.mainloop() # Wait for user to close window