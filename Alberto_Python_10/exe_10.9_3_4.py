import turtle

def sierpinski( tortoise, order, size, colorChangeDepth = -1 ) :
    colors = ['red','blue','magenta']
    if order == 0 :

        for k in range(3) :
        
            tortoise.forward( size )
            tortoise.left(120)

    else :

        for k in range(3) :

            if colorChangeDepth == 0 :
                tortoise.color( colors[k] )
            if  k == 1 :
                tortoise.penup()
                tortoise.forward( size/2 )
                tortoise.pendown()
            elif k == 2 :
                tortoise.left(120)
                tortoise.penup()
                tortoise.forward( size/2 )
                tortoise.pendown()
                tortoise.right(120)
            sierpinski( tortoise, order-1, size/2, colorChangeDepth-1 )
            if k == 2 :
                tortoise.right( 120 )
                tortoise.penup()
                tortoise.forward( size/2 )
                tortoise.pendown()
                tortoise.left(120)

win = turtle.Screen()
win.bgcolor('lightgreen')
win.setup(width=1980, height=1020, startx=0, starty=0)

frank = turtle.Turtle()
frank.speed(0)
frank.hideturtle

sierpinski( frank, 4, 200, 2 )

win.mainloop()