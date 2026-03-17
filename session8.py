# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 15:08:08 2025

@author: shiva
"""
#week3
#returns value
#to let a function a value,use the return statement:
def my_function(x):
    y=x*5
    return y
my_function(5)
###############################
def my_function(x):
    y=x*5
    z=x*7
    return y,z
my_function(5)
##################################
#Pass function
def my_function():
    passmy_function()
    
#recurssion function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)
###############################
#lambda function











add= lambda a:a+10
print(add (5,6))

###########################
#finding odd numbers from the list
lst = [34,12,64,55,75,13,63]
odd_lst = list(filter(lambda x : (x%2 !=0),lst))
print(odd_lst)
##################
#find out even numbers
lst = [34,12,64,55,75,13,61]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)




    
    
    