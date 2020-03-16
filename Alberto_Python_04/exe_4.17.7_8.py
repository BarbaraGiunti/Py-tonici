def to_secs( hours, minutes, seconds ) :
    return int( (hours * 60 ** 2) + (minutes * 60) + seconds )

print( to_secs(2, 30, 10) == 9010 )
print( to_secs(2, 0, 0) == 7200 )
print( to_secs(0, 2, 0) == 120 )
print( to_secs(0, 0, 42) == 42 )
print( to_secs(0, -10, 10) == -590 )

print( to_secs(2.5, 0, 10.71) == 9010 )
print( to_secs(2.433,0,0) == 8758 )