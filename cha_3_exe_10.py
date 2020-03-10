"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.hideturtle()
tess.color("blue")

for _ in range(5) :
    tess.forward(100)
    tess.right(360-2*108)

window.mainloop()