import turtle

def draw_square(animal, size):
    """
    Make animal draw a square with sides of length size.
    """
    for _ in range(4):
        animal.forward(size)
        animal.left(90)


window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")
window.title("Alex meets a function")

alex = turtle.Turtle() # Create alex
draw_square(alex, 50) # Call the function to draw the square
window.mainloop()