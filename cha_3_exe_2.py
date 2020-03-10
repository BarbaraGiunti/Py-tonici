"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

days = [ (0,"Sunday"), (1,"Monday"), (2,"Tuesday"), (3,"Wednesday"), (4,"Thursday"), (5,"Friday"), (6,"Saturday") ]

x = int( input("Insert the number of the day you left: ") )
y = int( input("Insert the number of days you are on vacation: ") )

z = ( x + y ) % 7
for number, name in days:
    if z == number:
        print("You will return home on ", name )
        break