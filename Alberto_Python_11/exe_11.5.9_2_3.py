import turtle
import random

class TurtleGTX( Turtle )

    def __init__( self ) :
        self.tortoise = turtle.Turtle()
        self.odo = 0
        self.tyre = True

    def forward( self, dist = 0 ) :
        if self.tyre :
            self.tortoise.forward( dist )
            if dist < 0 :
                delta = -dist
            else :
                delta = dist
            self.odo += delta
            prob_break = delta / 40000
            rng = random()
            if rng < prob_break :
                self.tyre = False
                print("The tyre broke.")
        else : 
            print("The tyre is broken and should be fixed.")

    def change_tyre( self ) :
        if self.tyre :
            print("The tyre is in a good shape.")
        else :
            self.tyre = True
            print("The tyre has been fixed.") 
