def days_in_month( name ) :
    if name == "January" or name == "March" or name == "May" or name == "July" or name == "August" or name == "October" or name == "December" :
        return 31
    if name == "November" or name == "April" or name == "June" or name == "September" :
        return 30
    if name == "February" :
        return 28
    return None

print( days_in_month("February") == 28 )
print( days_in_month("December") == 31 )