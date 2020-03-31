def mirror( word ) :

    L = len( word )
    mir_word = word
    for idx in range( 1, L+1 ) :
        mir_word += word[-idx]

    return mir_word

print( mirror("good") == "gooddoog" )
print( mirror("Python") == "PythonnohtyP" )
print( mirror("") == "" )
print( mirror("a") == "aa" )