def flatten( nested_list ):
    simple_list = []
    for element in nested_list:

        if type(element) is list:
            for nested_elem in element :
                simple_list.append( nested_elem )
        else:
            simple_list.append( element )

    return simple_list

print( flatten( [11, 2, [11, 13], 8] ) )
