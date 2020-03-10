"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in numbers :
    print(number)

for number in numbers :
    print(number, "\t", number**2)

total = 0
for number in numbers :
    total += number
print(total)

prod = 1
for number in numbers :
    prod = prod * number
print(prod)