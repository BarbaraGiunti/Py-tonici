import string

def replace_sub_word( word, before, after ) :

    L_before = len( before )
    idx = word.find( before, 0 )
    if idx < 0 :
        return word
    else :
        return word[0:idx] + after + word[idx+L_before:]




def replace_sub_word_all( word, before, after ) :

    new_word = replace_sub_word( word, before, after )
    while new_word != word :
        word = new_word
        new_word = replace_sub_word( word, before, after )

    return new_word




def replace( text, before, after ) :

    words = text.split()
    new_words = []
    for word in words :
        new_words.append( replace_sub_word_all( word, before, after )   )
    return " ".join( new_words )




print( replace("Mississippi", "i", "I") == "MIssIssIppI" )

song = "I love spom! Spom is my favorite food. Spom, spom, yum!" 
print( replace(song, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!" )

print( replace(song, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!" )