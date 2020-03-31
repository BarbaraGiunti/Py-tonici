def remove_vowels(phrase):
    vowels = "aeiou"
    string_sans_vowels = "" #inizializza la stringa finale senza vocali
    for letter in phrase:
        if letter.lower() not in vowels: #check che la lettera (in lower case) non sia una vocale
            string_sans_vowels += letter #concatena la stringa finale con la nuova lettera
    return string_sans_vowels

initial_word = "Fare python con i colleghi è estremamente divertente."
final_word = remove_vowels(initial_word)
print(final_word)