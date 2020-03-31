def add_vectors( vector1, vector2 ) :

    L = len( vector1 )
    S = []
    for idx in range(0,L) :
        S.append( vector1[idx] + vector2[idx] )
    return S




def scalar_mult( scalar, vector ) :

    L = len( vector )
    P = []
    for idx in range(0,L) :
        P.append( scalar * vector[idx] )
    return P




def dot_product( vec1, vec2 ) :

    L = len( vec1 )
    P = 0
    for idx in range(0,L) :
        P += vec1[idx] * vec2[idx] 
    return P




def cross_product( vec1, vec2 ) :

    P = []
    P.append( ( vec1[1] * vec2[2] ) - ( vec1[2] * vec2[1] ) )
    P.append( ( vec1[2] * vec2[0] ) - ( vec1[0] * vec2[2] ) )
    P.append( ( vec1[0] * vec2[1] ) - ( vec1[1] * vec2[0] ) )
    return P




print( add_vectors([1, 1], [1, 1]) == [2, 2] )
print( add_vectors([1, 2], [1, 4]) == [2, 6] )
print( add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4] )   

print( scalar_mult(5, [1, 2]) == [5, 10] )
print( scalar_mult(3, [1, 0, -1]) == [3, 0, -3] )
print( scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14] )

print( dot_product([1, 1], [1, 1]) == 2 )
print( dot_product([1, 2], [1, 4]) == 9 )
print( dot_product([1, 2, 1], [1, 4, 3]) == 12 )

print( cross_product([1, 2, 1], [1, 4, 3]) )