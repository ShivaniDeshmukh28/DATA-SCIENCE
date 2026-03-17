# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 16:15:33 2025

@author: shiva
"""

lst=[13,4,6,8,9]
num=int(input("Enter the number from list:"))
if num in lst:
    start=lst.index(num)
    print(*lst [start:])
    
#Search value in list
lst=[13,4,6,8,9]
num=int(input("Number to be return:"))
def search_num(lst, num):
    for i in range(len(lst)):
        if lst[i]==num:
            return "value found"
    return "value not found"
print(search_num(lst,num))
#######################
#count the vowels
input_string=input("Enter the string:")
def count_vowels(input_string):
    count=0
    input_string=input_string.lower()
    for i in range(len(input_string)):
        if input_string[i] in('a','e','i','o','u'):
            count=count+1
    return count
count_vowels(input_string)        

#####################
lst=[1,2,5,15,7,42]
total=0
for i in range(len(lst)):
    if lst[i]%5==0 and lst[i]%7==0:
        total=total+lst[i]
print(total)

##############################
#write a function that takes list and return either true if
#Duplicate found else return false
lst=[2,5,7,7,9]
def find_dup(lst):
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            return True
    return False
find_dup(lst)

#####################################
#write a program to count the number of digits in a number
num=int(input('Enter the number:'))
count=0
while(num!=0):
    digit=num%10
    count=count+1
    num=num//10
print(count)
