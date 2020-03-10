# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""

# WARNING: l'indentazione è fondamentale!!!
for friend in ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]:
    invite = "Hi " + friend + ". Please come to my party!"
    print(invite)
# il comando "break" fa uscire direttamente dal loop
# il comando "continue" invece fa terminare l'iterazione corrente e ciclo e passa alla successiva

# Se volessimo disegnare un quadrato 
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen") 
window.title("Square") 

alex = turtle.Turtle()

# primo modo
for i in [0,1,2,3]: # equivalente a --> for i in range(4) :
    alex.forward(50)
    alex.left(90)

# modo da informatico A++, visto che non usiamo mai il counter i
for _ in range(4):
    alex.penup()
    alex.forward(100) # This moves alex, but no line is drawn
    alex.left(90)
    alex.pendown()
    

# visto che non usiamo il counter per disgnare il quadrato possiamo usarlo per fare altro!
alex.shape("turtle") # Cambia forma ad Alex
alex.speed(1) # Cambia velocità ad Alex: 1 minimo, 10 massimo, 0 significa no animazione
colors = ["yellow", "red", "purple", "blue"] # Assign a list to a variable
for color in colors:
    alex.color(color)
    alex.forward(50)
    alex.left(90)

window.mainloop()