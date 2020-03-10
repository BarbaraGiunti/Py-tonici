"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

step = 100
diag = step * ( 2 ** 0.5 )
moves = [ (0,step), (135,diag), (-90,diag/2), (-90,diag/2), (-90,diag), (-135,step), (-90,step), (-90,step) ]

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.hideturtle()
tess.pensize(3)
tess.color("blue")

for degs, steps in moves :
    tess.left(degs)
    tess.forward(steps)

window.mainloop()