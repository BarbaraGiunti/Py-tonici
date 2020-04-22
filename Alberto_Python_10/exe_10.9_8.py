def fib( n ) :
    if n < 3 :
        return 1
    else :
        f_0 = 1
        f_1 = 1
        f_2 = 2
        for k in range( 3, n ) :
            f_0 = f_1
            f_1 = f_2
            f_2 = f_0 + f_1
        return f_2

print( fib(200) )