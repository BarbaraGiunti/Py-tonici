def reverse( word ) :

    L = len( word )
    rev_word = ""
    for idx in range( 1, L+1 ) :
        rev_word += word[-idx]

    return rev_word




def is_palindrome( word ) :

    return word == reverse( word )




print( is_palindrome("abba") )
print( not is_palindrome("abab") )
print( is_palindrome("tenet") )
print( not is_palindrome("banana") )
print( is_palindrome("straw warts") )
print( is_palindrome("a") )