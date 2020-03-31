prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter.lower() in "oq":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)