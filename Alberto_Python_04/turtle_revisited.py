import turtle

def make_window(color, title):
    """
    Set up the window with the given background color and title.
    Returns the new window.
    """
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window

def make_turtle(color, size):
    """
    Set up a turtle with the given color and pensize.
    Returns the new turtle.
    """
    animal = turtle.Turtle()
    animal.color(color)
    animal.pensize(size)
    return animal


wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

wn.mainloop()