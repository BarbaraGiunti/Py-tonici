import turtle

def make_square( animal, size ) :
    for _ in range(4) :
        animal.forward(size)
        animal.left(90)

def draw_4_squares( animal, size ) :
    for _ in range(4) :
        make_square( animal, size )
        animal.left( 90 )

wndw = turtle.Screen()
wndw.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("blue")
tess.speed(10)

for _ in range(5) :
    draw_4_squares( tess, 100 )
    tess.left(90/5)

wndw.mainloop()