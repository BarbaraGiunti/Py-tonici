import turtle

def draw_poly( t, n, sz ) :
    for _ in range(n) :
        t.forward(sz)
        t.left(360/n)

wndw = turtle.Screen()
wndw.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")

draw_poly( tess, 8, 50 )

wndw.mainloop()