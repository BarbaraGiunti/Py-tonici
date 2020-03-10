"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

x = float( input("Insert the lenght of the first side: ") )
y = float( input("Insert the lenght of the second side: ") )
z = float( input("Insert the lenght of the third side: ") )

threshold = 1e-7
temp = ( x**2 ) + ( y**2 ) + ( z**2 )
if z > y :
    if z > x:
        temp = ( temp - ( z**2 ) ) ** 0.5
        check = abs( z - temp ) < threshold
    else :
        temp = ( temp - ( x**2 ) ) ** 0.5
        check = abs( x - temp ) < threshold
else :
    if y > x :
        temp = ( temp - ( y**2 ) ) ** 0.5
        check = abs( y - temp ) < threshold
    else :
        temp = ( temp - ( x**2 ) ) ** 0.5
        check = abs( x - temp ) < threshold

print("The given triangle is rectangle: ", check )