with open("numbered_sample.txt","r") as numbered_file:
    all_lines = numbered_file.readlines()

with open("unnumbered_sample.txt", "w") as unnumbered_file:
    for line in all_lines :
        unnumbered_file.write( line[5:] )