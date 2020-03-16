import turtle

def draw_poly( t, n, sz ) :
    for _ in range(n) :
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle( t, sz ) :
    draw_poly( t, 3, sz )

wndw = turtle.Screen()
wndw.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")

draw_equitriangle( tess, 50 )

wndw.mainloop()