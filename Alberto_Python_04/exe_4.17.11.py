def compare( a, b ) :
    if a > b :
        return 1
    if a == b :
        return 0
    if a < b :
        return -1
    return None

print( compare(5, 4) == 1 )
print( compare(7, 7) == 0 )
print( compare(2, 3) == -1 )
print( compare(42, 1) == 1 )