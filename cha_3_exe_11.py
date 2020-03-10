"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.pensize(2)

tess.stamp()
for _ in range(12) :
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(10)
    tess.stamp()
    tess.backward(120)
    tess.left(360/12)
    tess.pendown()

window.mainloop()