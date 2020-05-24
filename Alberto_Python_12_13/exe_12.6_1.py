import math

def readposint():

    user_input = input("Please enter a positive integer:")

    digits = {'0','1','2','3','4','5','6','7','8','9'}
    pos = True
    decim = False

    nnum = ValueError('You did not enter a number.')

    int_digits = 0
    decim_digits = 0
    number = 0.0
    for char in user_input:
        if char in digits:
            if decim:
                decim_digits += 1
                number += int(char) / ( 10**decim_digits )
            else:
                int_digits += 1
        elif char == '-':
            if pos and int_digits == 0:
                pos = False
            else:
                raise nnum
        elif char == '.':
            if not(decim):
                decim = True
            else:
                raise nnum
        else:
            raise nnum

    if pos:
        shift = 0
    else:
        shift = 1    
    for k in range(int_digits):
        number += int( user_input[k+shift] ) * ( 10**(int_digits-k-1) )

    if not(pos):
        npos = ValueError('You entered a non-positive number.')
        raise npos
    if decim_digits > 0:
        nint = ValueError('You entered a non-integer number.')
        raise nint
    print('You indeed entered a positive integer: {0}.'.format(int(number)) )

readposint()