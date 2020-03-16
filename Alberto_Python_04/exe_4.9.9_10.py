import turtle

def draw_star( t, sz ) :
    for _ in range(5) :
        t.forward(sz)
        t.right(144)

wndw = turtle.Screen()
wndw.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")

for _ in range(5) :
    draw_star( tess, 100 )
    #tess.penup()
    tess.forward(350)
    tess.right(144)
    #tess.pendown()

wndw.mainloop()