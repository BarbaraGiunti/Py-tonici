text = """
Il primo risultato della ricerca python su google è
http://www.python.org/ . La storia matta è che
devo infilare in questa frase qualcosa tra minore e maggiore
tipo <qualcosa>. Ecco l'ho fatto.
"""

print( text )

def get_url( text ) :
     
    words = text.split()
    for word in words :
        if word.find( "http://", 0 ) == 0 :
            return word
    return ""

def get_brackets( text ) :
     
    idx_start = text.find("<")
    idx_stop = text.find(">")
    if idx_start < idx_stop :
        return text[idx_start+1:idx_stop]
    return ""

print( get_url( text ) )

print( get_brackets( text ) )
