def remove( sub_string, string ) :

    sub_L = len( sub_string )
    idx = string.find( sub_string, 0 )
    if idx < 0 :
        return string
    else :
        return string[0:idx] + string[idx+sub_L:]




def remove_all( sub_string, string ) :

    new_string = remove( sub_string, string )
    while new_string != string :
        string = new_string
        new_string = remove( sub_string, string )

    return new_string




print( remove("an", "banana") == "bana" )
print( remove("cyc", "bicycle") == "bile" )
print( remove("iss", "Mississippi") == "Missippi" )
print( remove("eggs", "bicycle") == "bicycle" )

print( remove_all("an", "banana") == "ba" )
print( remove_all("cyc", "bicycle") == "bile" )
print( remove_all("iss", "Mississippi") == "Mippi" )
print( remove_all("eggs", "bicycle") == "bicycle" )