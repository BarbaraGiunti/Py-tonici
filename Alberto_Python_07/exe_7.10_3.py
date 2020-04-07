with open("sample.txt","r") as file:
    all_lines = file.readlines()

with open("numbered_sample.txt", "w") as numbered_file:
    count = 0
    for line in all_lines :
        count += 1
        if count < 10 :
            numbered_file.write( "000{0} ".format( count ) + line )
        elif count < 100 :
            numbered_file.write( "00{0} ".format( count ) + line )
        elif count < 1000 :
            numbered_file.write( "0{0} ".format( count ) + line )
        else :
            numbered_file.write( "{0} ".format( count ) + line )