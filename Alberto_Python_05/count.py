def count_a(text):
    count = 0
    for letter in text:
        if letter == "a":
            count += 1
    return(count)

print(count_a("banana") == 3)