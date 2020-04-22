import turtle

def koch(tortoise, order, size):
    if order == 0:
        tortoise.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(tortoise, order-1, size/3)
            tortoise.left(angle)

win = turtle.Screen()
win.bgcolor('lightgreen')
frank = turtle.Turtle()
frank.color('blue')
frank.speed(0)
frank.hideturtle()

for k in range(3) :
    koch( frank, 2, 200 )
    frank.right(120)

win.mainloop()