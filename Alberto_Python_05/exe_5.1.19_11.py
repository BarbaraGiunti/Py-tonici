def count( sub_string, string ) :
    sub_L = len( sub_string )
    ct = 0
    idx = string.find( sub_string, 0 )
    while idx >= 0 :
        ct += 1
        idx = string.find( sub_string, idx+1 )
    return ct
 
print( count("is", "Mississippi") == 2 )
print( count("an", "banana") == 2 )
print( count("ana", "banana") == 2 )
print( count("nana", "banana") == 1 )
print( count("nanan", "banana") == 0 )
print( count("aaa", "aaaaaa") == 4 )