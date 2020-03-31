import string

#carico il libro dal txt
Alice = open('alice_book.txt', 'r')
alice_book = Alice.read()
Alice.close()

#creo una versione lowercase senza punteggiatura del libro
alice_new = ""
for letter in alice_book:
    if letter not in string.punctuation:
        alice_new += letter.lower()

#apro il file destinazione
alice_words = open("alice_words.txt", "w")

#setto il layout delle righe del dizionario e stampo le due righe di intestazione
layout = "{0:<28}{1:<7}\n"
alice_words.write( layout.format( "Word", "Count" ) )
alice_words.write( "===================================\n" )

#divido il libro in parole e creo il dizionario vuoto
words = alice_new.split()
word_count = {}

#conto l'occorrenza delle parole
for word in words :
    word_count[ word ] = word_count.get( word, 0 ) + 1

#creo una lista dal dizionario, la riordino e la stampo
word_items = list( word_count.items() )
word_items.sort()
longest = word_items[0][0]
L = len( longest )
for item in word_items :
    alice_words.write( layout.format( item[0], item[1] ) )
    if len( item[0] ) > L :
        longest = item[0]
        L = len( item[0] )

#chiudo il file destinazione
alice_words.close()

#numero di occorrenze di Alice
print( word_count["alice"] )

#parola più lunga e lunghezza
print( longest, "\t", L )