import random

def make_random_ints(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between lower_bound
    and upper_bound. upper_bound is an open bound.
    """
    rng = random.Random() # Create a random number generator
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

print( make_random_ints(5, 1, 13) ) # Pick 5 random month numbers

# if we don't want repetition we can do the following

xs = list(range(1,13)) # Make list 1..12 (there are no duplicates)
rng = random.Random() # Make a random number generator
rng.shuffle(xs) # Shuffle the list
result = xs[:5] # Take the first five elements
print( result )

# however if the range is huge this is very inefficient and it is better to do the following

def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
    Generate a list containing num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    The result list cannot contain duplicates.
    """
    result = []
    rng = random.Random()
    temp = upper_bound - lower_bound
    if num > temp :
        num = temp
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)

xs = make_random_ints_no_dups(10, 1, 6)
print(xs)