#-----------------------------------------------------
# CLASS AND MODULES
#-----------------------------------------------------

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__( self, x = 0, y = 0 ):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def reflect_x(self) :
        return Point( self.x, -self.y )

    def slope_from_origin( self ) :
        if self.x == 0 :
            return "Inf"
        else:
            return self.y / self.x

    def get_line_to( self, target ) :
        dx = self.x - target.x
        dy = self.y - target.y
        if dx == 0 :
            return Point( "Inf", self.x )
        else :
            m = dy / dx
            q = self.y - self.x * m
            return Point(m,q)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self) :
        return self.width * self.height

    def perimeter(self) :
        return 2 * ( self.width + self.height )

    def flip(self) :
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains( self, p ) :
        if self.width < 0 :
            min_x = self.corner.x + self.width
            max_x = self.corner.x
        else :
            min_x = self.corner.x 
            max_x = self.corner.x + self.width

        if self.height < 0 :
            min_y = self.corner.y + self.height
            max_y = self.corner.y
        else :
            min_y = self.corner.y 
            max_y = self.corner.y + self.height

        check_x = ( min_x <= p.x ) and ( p.x < max_x  )
        check_y = ( min_y <= p.y ) and ( p.y < max_y )
        
        return check_x and check_y

#---------------------------------------------------
# FUNCTIONS
#---------------------------------------------------

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

def collide( r1, r2 ) :
    A = r1.corner
    B = Point( A.x + r1.width, A.y )
    C = Point( A.x + r1.width, A.y + r1.height  )
    D = Point( A.x, A.y + r1.height )
    if r2.contains( A ) or r2.contains( B ) or r2.contains( C ) or r2.contains( D ) :
        return True
    else :
        return False

#----------------------------------------------------
# SCRIPT
#----------------------------------------------------

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box)
print("bomb: ", bomb)

r = Rectangle(Point(10,5), 100, 50)
print(r)
r.grow(25, -10)
print(r)
r.move(-10, 10)
print(r)

p1 = Point(3, 4)
p2 = Point(3, 4)
same_coordinates(p1, p2)

#--------------------------------------------------------
# EXE 1 
#----------------------------------------------------

r = Rectangle(Point(0, 0), 10, 5)
print(r.area() == 50)

#--------------------------------------------------------
# EXE 2
#----------------------------------------------------

r = Rectangle(Point(0, 0), 10, 5)
print(r.perimeter() == 30)

#--------------------------------------------------------
# EXE 3
#----------------------------------------------------

r = Rectangle(Point(100, 50), 10, 5)
print(r.width == 10 and r.height == 5)
r.flip()
print(r.width == 5 and r.height == 10)

#--------------------------------------------------------
# EXE 4
#----------------------------------------------------

r = Rectangle(Point(0, 0), 10, 5)
print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(not r.contains(Point(3, 7)))
print(not r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.99999)))
print(not r.contains(Point(-3, -3)))

#--------------------------------------------------------
# EXE 5
#----------------------------------------------------

r1 = Rectangle(Point(0, 0), 10, 5)
r2 = Rectangle(Point(-1, -1), 10, 5)
print( collide( r1, r2 ) )
r3 = Rectangle(Point(-1, -1), 0.5, 0.5)
print( collide( r1, r3 ) )