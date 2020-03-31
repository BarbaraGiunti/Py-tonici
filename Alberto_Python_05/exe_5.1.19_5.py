text = """Lorem ipsum dolor sit amet, consectetur adipisci elit, 
sed do eiusmod tempor incidunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrum exercitationem ullamco laboriosam, 
nisi ut aliquid ex ea commodi consequatur. Duis aute irure reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint obcaecat cupiditat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum."""

import string

def elaborate_text( text ):

    text_wo_punct = ""

    for letter in text :
        if letter not in string.punctuation :
            text_wo_punct += letter

    text_new = text_wo_punct.split()
    count_tot = len( text_new )

    count_e = 0
    for word in text_new :
        if "e" in word :
            count_e += 1

    return count_tot, count_e

count_tot, count_e = elaborate_text( text )
print('Your text contains {0} words, of which {1} ({2}%) contain an "e".'.format( count_tot, count_e, 100*count_e/count_tot ))