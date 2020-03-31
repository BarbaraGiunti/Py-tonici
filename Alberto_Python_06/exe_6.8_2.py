import numpy as np

a = np.array( [ 230, 10, 284, 39, 76 ] )

while a.min() < 100 :
    a[ a < 100 ] = 2 * a[ a < 100 ]

b = a[ a > 150 ]
b = b[ b < 200 ]
print( b )