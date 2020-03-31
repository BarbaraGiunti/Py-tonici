word = "banana"
count = 0
for letter in word:
     if letter == "a":
        count += 1
print(count)

#exe 3
def count_letters( string, letter ):
    count = 0
    for character in string:
        if character == letter:
            count += 1
    return count

count = count_letters( word, "a" )
print(count)

#exe 4
def count_letters( string, letter ):
    count = 0
    idx = string.find(letter, 0)
    while idx >= 0:
        count += 1
        idx = string.find(letter, idx+1)
    return count

count = count_letters( word, "a" )
print(count)