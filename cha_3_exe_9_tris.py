"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

n = 23

check = 0
k = 2
while check == 0 :

    if n % k == 0 :
        check = 1
    else :
        k += 1

    if k == n :
        break

print( check == 0 )