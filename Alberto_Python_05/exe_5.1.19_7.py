def reverse( word ) :

    L = len( word )
    rev_word = ""
    for idx in range( 1, L+1 ) :
        rev_word += word[-idx]

    return rev_word

print( reverse("happy") == "yppah" )
print( reverse("Python") == "nohtyP" )
print( reverse("") == "" )
print( reverse("a") == "a" )