def remove_letter( letter, word ) :

    new_word = ""
    for character in word :
        if character != letter :
            new_word += character

    return new_word

print( remove_letter("a", "apple") == "pple" )
print( remove_letter("a", "banana") == "bnn" )
print( remove_letter("z", "banana") == "banana" )
print( remove_letter("i", "Mississippi") == "Msssspp" )
print( remove_letter("b", "") == "" )
print( remove_letter("b", "c") == "c" )