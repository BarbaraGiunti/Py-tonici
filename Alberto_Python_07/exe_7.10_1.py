with open("sample.txt","r") as file:
    all_lines = file.readlines()

with open("reverse_sample.txt", "w") as reverse_file:
    for k in range( 1, len( all_lines )+1 ):
        reverse_file.write( all_lines[-k] )