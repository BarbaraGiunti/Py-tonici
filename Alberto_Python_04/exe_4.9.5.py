import turtle

def draw_spiral( animal, angle, n_sides ) :
    size = 1
    for _ in range( n_sides ) :
        animal.forward( size )
        animal.right( angle )
        size += 5

wndw = turtle.Screen()
wndw.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pensize(3)
alex.color('blue')
alex.speed(10)

# prima figura con (90,100) seconda con (89,100)
draw_spiral( alex, 89, 100 )

wndw.mainloop()