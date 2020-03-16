import turtle

def make_square( animal, size ) :
    for _ in range(4) :
        animal.forward(size)
        animal.left(90)

win1 = turtle.Screen()
win1.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)
alex.color("hotpink")

for _ in range(5) :
    make_square( alex, 20 )
    alex.penup()
    alex.forward(40)
    alex.pendown()

win1.mainloop()



