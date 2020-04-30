#-----------------------------------------------------
# CLASS AND MODULES
#-----------------------------------------------------

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__( self, x = 0, y = 0 ):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)

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

    def reverse(self):
        (self.x , self.y) = (self.y, self.x)

#-------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------

def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

def distance(p1,p2) :
    return ( ( (p1.x-p2.x)**2 ) + ( (p1.y-p2.y)**2 ) ) ** 0.5

def circle_center( p1, p2, p3, p4 = "None" ) :
    if p4 == "None" :
        a1_1 = p2.x - p1.x
        a1_2 = p2.y - p1.y
        a2_1 = p3.x - p1.x
        a2_2 = p3.y - p1.y
        det = ( a1_1 * a2_2 ) - ( a1_2 * a2_1 )
        if det == 0 :
            return "None"
        else:
            b1 = (p2.x**2) + (p2.y**2) - (p1.x**2) - (p1.y**2)
            b2 = (p3.x**2) + (p3.y**2) - (p1.x**2) - (p1.y**2)
            c1 = ( ( a2_2 * b1 ) - ( a1_2 * b2) ) / ( 2 * det )
            c2 = ( ( a1_1 * b2 ) - ( a2_1 * b1) ) / ( 2 * det )
            return Point(c1,c2)
    else :
        c1 = circle_center( p1, p2, p3 )
        c2 = circle_center( p1, p2, p4 )
        if c1 == "None" or c2 == "None" :
            return "None"
        elif c1.x == c2.x and c1.y == c2.y :
            return c1
        else:
            return "None"
            

#----------------------------------------------------
# SCRIPT
#----------------------------------------------------

p = Point(3,4) # Instantiate an object of type Point
q = Point(5,12) # Make a second point
r = Point()

print(p.x, q.y, r.x) # Each point object has its own x and y

print_point(p)
str( p )

print( p.distance_from_origin() )

p = Point(3, 4)
q = Point(5, 12)
print( midpoint(p,q) )
print( p.halfway(q) )

#-------------------------------------------------
# EXE 1
#-------------------------------------------------

print( distance(p,q) )

#-------------------------------------------------
# EXE 2
#-------------------------------------------------

print( Point(3,5).reflect_x() )

#-------------------------------------------------
# EXE 3
#-------------------------------------------------

print( Point(4,10).slope_from_origin() )
print( Point(0,10).slope_from_origin() )

#-------------------------------------------------
# EXE 4
#-------------------------------------------------

print( Point(4,11).get_line_to(Point(6,15)) )
print( Point(4,11).get_line_to(Point(4,15)) )

#-------------------------------------------------
# EXE 5
#-------------------------------------------------

p1 = Point(1,0)
p2 = Point(0,1)
p3 = Point(-1,0)
print( circle_center(p1,p2,p3) )
print( circle_center(p1,p2,p3,Point(0,-1)) )
print( circle_center(p1,p2,p3,Point(2,0)) )