"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for Mark in numbers :
    if Mark >= 75 :
        print("Mark: ", Mark, "\t Grade: First")
    elif Mark >= 70 :
        print("Mark: ", Mark, "\t Grade: Upper Second")
    elif Mark >= 60 :
        print("Mark: ", Mark, "\t Grade: Second")
    elif Mark >= 50 :
        print("Mark: ", Mark, "\t Grade: Third")
    elif Mark >= 45 :
        print("Mark: ", Mark, "\t Grade: F1 Supp")
    elif Mark >= 40 :
        print("Mark: ", Mark, "\t Grade: F2")
    else : 
        print("Mark: ", Mark, "\t Grade: F3")