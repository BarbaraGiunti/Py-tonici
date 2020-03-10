"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

numbers = [ 1, -2, -3, 4, 5, -6 ]

count_odd = 0
sum_eve = 0
sum_neg = 0
for n in numbers :

    if n % 2 == 1 :
        count_odd += 1
    else :
        sum_eve += n

    if n < 0 :
        sum_neg += n

print("There are ", count_odd, "odd numbers.")
print("The sum of the even numbers is ", sum_eve)
print("The sum of the negative numbers is ", sum_neg)
    
sum_odd = 0
for n in numbers :

    if n % 2 == 1 :
        sum_odd += n
    else :
        break

print("The sum of the first odd streak is ", sum_odd)

sum_squares = 0
for n in numbers :
    sum_squares += n ** 2

print("The sum of the squares is ", sum_squares)