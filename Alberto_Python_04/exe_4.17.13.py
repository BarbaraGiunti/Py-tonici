def slope( x1, y1, x2, y2 ) :
    if x2 - x1 == 0 :
        return None
    else :
        return (y2 - y1) / (x2 - x1)

def intercept( x1, y1, x2, y2 ) :
    if x2 - x1 == 0 :
        return None
    else :
        m = slope( x1, y1, x2, y2 )
        return y1 - m * x1

print( slope(5, 3, 4, 2) == 1.0 )
print( slope(1, 2, 3, 2) == 0.0 )
print( slope(1, 2, 3, 3) == 0.5 )
print( slope(2, 4, 1, 2) == 2.0 )

print( intercept(1, 6, 3, 12) == 3.0 )
print( intercept(6, 1, 1, 6) == 7.0 )
print( intercept(4, 6, 12, 8) == 5.0 )