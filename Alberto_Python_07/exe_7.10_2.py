with open("sample.txt","r") as file:
    all_lines = file.readlines()

for line in all_lines:
    if "snake" in line :
        print( line )