import turtle

def make_square( animal, size ) :
    for _ in range(4) :
        animal.forward(size)
        animal.left(90)

win2 = turtle.Screen()
win2.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)
alex.color("hotpink")

for k in range(5) :
    make_square( alex, 20 + k*20 )
    alex.penup()
    alex.backward(10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.pendown()

win2.mainloop()