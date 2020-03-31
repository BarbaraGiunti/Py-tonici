import string

def count_letters( text ) :

    letter_count = {}

    words = text.split()
    for word in words :
        for letter in word.lower() :
            letter_count[letter] = letter_count.get( letter, 0 ) + 1

    letter_items = list( letter_count.items() )
    letter_items.sort()
    for item in letter_items :
        print( item[0], "\t", item[1] )




text = "ThiS is String with Upper and lower case Letters"
count_letters( text )