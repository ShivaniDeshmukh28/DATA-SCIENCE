# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 18:30:29 2025

@author: shiva
"""
#create list it contains 0 to 19 numbers
lst=[]
for num in range(0,20):
    lst.append(num)
print(num)
print(lst)
                    #OR

#create list it contains 0 to 19 numbers
lst=[num for num in range(0,20)]
print(lst)

#perform capitalization of strings
names=['dada','kaka','mama','papa']
lst=[name.capitalize() for name in names]
print(lst)

#Find even numbers using lst
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num) ]
print(lst)

#List comprehension
evens=[num for num in range(10) if num%2==0]
print(evens)
