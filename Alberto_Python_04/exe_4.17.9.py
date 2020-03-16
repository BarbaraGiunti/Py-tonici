def hours_in( secs ) :
    return int( secs / ( 60 ** 2 ) )

def minutes_in( secs ) :
    temp = secs - ( hours_in( secs ) * 60 ** 2 )
    return int( temp / 60 )

def seconds_in( secs ) :
    temp = secs - ( hours_in( secs ) * 60 ** 2 ) - ( minutes_in( secs ) * 60 )
    return temp

print( hours_in(9010) == 2 )
print( minutes_in(9010) == 30 )
print( seconds_in(9010) == 10 )