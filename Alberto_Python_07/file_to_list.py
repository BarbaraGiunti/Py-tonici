with open("test.txt", "r") as input_file:
    all_lines = input_file.readlines()
    all_lines.sort()

with open("sortedtest.txt", "w") as output_file:
    for line in all_lines:
        output_file.write(line)