def f2c(t) :
    temp = 5 * ( t - 32 ) / 9
    return round( temp, 0 )

def c2f(t) :
    temp = 32 + t * 9 / 5
    return round( temp, 0 )

print( f2c(212) == 100 ) # Boiling point of water
print( f2c(32) == 0 ) # Freezing point of water
print( f2c(-40) == -40 ) # Wow, what an interesting case!
print( f2c(36) == 2 )
print( f2c(37) == 3 )
print( f2c(38) == 3 )
print( f2c(39) == 4 )

print( c2f(0) == 32 )
print( c2f(100) == 212 )
print( c2f(-40) == -40 )
print( c2f(12) == 54 )
print( c2f(18) == 64 )
print( c2f(-48) == -54 )