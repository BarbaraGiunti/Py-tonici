def find2(haystack, needle, start=0, end=-1): #start (end) è un parametro opzionale che viene messo a 0 se non dato dall'utente
    for index,letter in enumerate(haystack[start:end]):
        if letter == needle:
            return index + start
    return -1

print(find2("banana", "a", 2) == 3)