leet_speak = {}
leet_speak["a"] = "4"
leet_speak["b"] = "8"
leet_speak["c"] = "("
leet_speak["d"] = "|)"
leet_speak["e"] = "3"
leet_speak["f"] = "|="
leet_speak["g"] = "6"
leet_speak["h"] = "|-|"
leet_speak["i"] = "|"
leet_speak["j"] = "_|"
leet_speak["k"] = "|<"
leet_speak["l"] = "1"
leet_speak["m"] = "|\/|"
leet_speak["n"] = "|\|"
leet_speak["o"] = "0"
leet_speak["p"] = "|°"
leet_speak["q"] = "0,"
leet_speak["r"] = "|^"
leet_speak["s"] = "5"
leet_speak["t"] = "7"
leet_speak["u"] = "|_|"
leet_speak["v"] = "\/"
leet_speak["w"] = "\/\/"
leet_speak["x"] = "%"
leet_speak["y"] = "'/"
leet_speak["z"] = "2"

with open("sample.txt","r") as old_file:
    all_lines = old_file.readlines()

with open("leet_sample.txt", "w") as leet_file:
    for line in all_lines :
        for letter in line :
            temp = letter.lower()
            if temp in leet_speak :
                leet_file.write( leet_speak[ temp ] )
            else :
                leet_file.write( letter )