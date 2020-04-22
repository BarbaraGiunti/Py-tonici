def count( nested_list, target ):
    total = 0
    for element in nested_list:

        if type(element) is list:
            total += count( element, target )
        else:
            if element == target :
                total += 1

    return total

print( count( [11, 2, [11, 11], 8], 11 ) )