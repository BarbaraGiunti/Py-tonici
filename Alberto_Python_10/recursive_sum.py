def recursive_sum(nested_number_list):
    """Returns the total sum of all elements in nested_number_list"""
    if len(nested_number_list) == 0:
        return 0
    head, *tail = nested_number_list #Assign the first element of nested_number_list
        #to head, and the rest to tail.
    if isinstance(head, list): # If head is a list....
        return recursive_sum(head) + recursive_sum(tail)
    else:
        return head + recursive_sum(tail)

def recursive_max(nested_list):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_max(element)
        else:
            value = element

        if first_time or value > largest:
            largest = value
            first_time = False

    return largest

print( recursive_sum( [1, 2, [11, 13], 8] ) )
print( recursive_max( [1, 2, [11, 13], 8] ) )