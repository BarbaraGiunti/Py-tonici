"""
@author: Alberto Viscardi
@date: 10/03/2020
"""

words = [ "salgemma", "filibustiere", "maremma", "sam", "mucca", "forlì" ]

count_5 = 0
count_sam = 0
find_sam = 0
for word in words :

    if len(word) == 5 :
        count_5 += 1

    if find_sam == 0 :
        count_sam += 1
        if word == "sam" :
            find_sam = 1

print("There are ", count_5, " words of length 5.")
print("Up to the first occurence of 'sam' there are", count_sam, " words")