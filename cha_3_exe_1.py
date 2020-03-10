"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

days = [ (0,"Sunday"), (1,"Monday"), (2,"Tuesday"), (3,"Wednesday"), (4,"Thursday"), (5,"Friday"), (6,"Saturday") ]

x = int( input("Insert today's number in the week: ") )
for number, name in days:
    if x == number:
        print("Today is ", name )
        break
else:
    print("Invalid number.")