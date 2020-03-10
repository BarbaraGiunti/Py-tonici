"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
spugna = turtle.Turtle()
spugna.shape("turtle")
spugna.color("blue")

movements = [ (160,20), (-43,10), (270,8), (-97,100), (-43,12), (200,100), (-940,100), (17,100), (-86,100)]

heading = 0
for degs, steps in movements :
    spugna.left(degs)
    spugna.forward(steps)
    heading = ( heading + degs ) % 360
print(heading)    

window.mainloop()