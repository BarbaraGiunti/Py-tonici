 # -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:37:38 2020

@author: Alberto Viscardi
"""

n = 25
threshold = 0.001 # Make this smaller for better accuracy
approximation = n/2 # Start with some or other guess at the answer
count = 0
while True:
    count += 1
    better = (approximation + n/approximation)/2
    print(better)
    if abs(approximation - better) < threshold:
        break
    approximation = better
print("The number of interations needed is ", count)