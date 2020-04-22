def recursive_min(nested_list):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    smallest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_min(element)
        else:
            value = element

        if first_time or value < smallest:
            smallest = value
            first_time = False

    return smallest

print( recursive_min( [11, 2, [1, 13], 8] ) )