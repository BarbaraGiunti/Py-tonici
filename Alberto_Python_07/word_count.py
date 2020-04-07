with open("test.txt") as f:
    content = f.read()

words = content.split()
print("There are {0} words in the file.".format(len(words)))