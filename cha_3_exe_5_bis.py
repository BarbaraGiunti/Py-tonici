"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
franco = turtle.Turtle()
franco.shape("turtle")
franco.color("blue")

side = 100
for k in [ 3, 4, 6, 8 ] :
    for _ in range(k) :
        franco.forward(side)
        franco.left(360/k)

window.mainloop()