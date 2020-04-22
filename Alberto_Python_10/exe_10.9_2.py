import turtle, numpy

def cesaro( tortoise, order, size, tear ) :
    if order == 0 :
        tortoise.forward( size )
    else:
        base_angle = ( 180 - tear ) / 2
        tear_rad = numpy.pi * tear / 180
        new_size = size / ( 2 * ( 1 + numpy.sin(tear_rad/2) ) ) 
        for angle in [base_angle, 180+tear, base_angle, 0] :
            cesaro( tortoise, order-1, new_size, tear )
            tortoise.right( angle )

def cesaro_closed( tortoise, order, size, tear ):
    for k in range(4):
        cesaro( tortoise, order, size, tear )
        tortoise.right(90)
    tortoise.penup()
    tortoise.forward( size )
    tortoise.pendown()

size = 50 
tear = 10

win = turtle.Screen()
win.bgcolor('lightgreen')
win.setup(width=1980, height=1020, startx=0, starty=0)

frank = turtle.Turtle()
frank.color('blue')
frank.speed(0)
frank.hideturtle
frank._tracer(False)


for k in range(4) :
    frank.penup()
    frank.forward( size + size**0.5 )
    frank.pendown()
    cesaro_closed( frank, k, size, tear )

win.mainloop()