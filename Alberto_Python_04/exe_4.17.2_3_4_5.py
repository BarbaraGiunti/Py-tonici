def day_name( num ) :
    if num == 0 :
        return 'Sunday'
    if num == 1 :
        return 'Monday'
    if num == 2 :
        return 'Tuesday'
    if num == 3 :
        return 'Wednesday'
    if num == 4 :
        return 'Thursday'
    if num == 5 :
        return 'Friday'
    if num == 6 :
        return 'Saturday'
    return None

def day_num( name ) :
    if name == 'Sunday' :
        return 0
    if name == 'Monday' :
        return 1
    if name == 'Tuesday' :
        return 2
    if name == 'Wednesday' :
        return 3
    if name == 'Thursday' :
        return 4
    if name == 'Friday' :
        return 5
    if name == 'Saturday' :
        return 6
    return None

def day_add( name, delta ) :
    num = day_num( name )
    return day_name( (num+delta) % 7 )


print( day_add("Monday", 4) == "Friday" )
print( day_add("Tuesday", 0) == "Tuesday" )
print( day_add("Tuesday", 14) == "Tuesday" )
print( day_add("Sunday", 100) == "Tuesday" )

print( day_add("Sunday", -1) == "Saturday" )
print( day_add("Sunday", -7) == "Sunday" )
print( day_add("Tuesday", -100) == "Sunday" )