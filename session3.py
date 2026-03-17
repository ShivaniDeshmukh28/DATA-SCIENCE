# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 14:59:16 2025

@author: shiva
"""
#Multiple variable initialization in one line
x,y,z=5,6,7
print(x)
print(y)
print(z)
x,y,z=5
print(x)
print(y)
print(z)

######################

#Global variable
x="awesome"
def my_function():
    print("Python is "+x)
my_function()

#######################

# Global and Local variables
x="Awesome"
def my_function():
    x="Fantastic"
    print("Python is "+x)
my_function()

##########################

#Range
x=range(6)
print(x)
print(type(x))
################

# dictionary
x={"name":"shiv","age":20}
print(type(x))

##############################

#List
lst= [1,2,3,4,5]
print(lst)
print(type(lst))

#############################

#Tuple
tup=(1,2,3,4)
print(tup)
print(type(tup))

##############################

#Set
set1={1,2,3,4,5,6}
print(set1)
print(type(set1))
***Set does not allow repeated elements***

###############################

# Concate
str1="Hello"
str2=2
str3=str1+str2
print(f"Hello{str2}")

#########################
#Strings
#If you want multiple strings
x="""this is python. It is very powerful."""
print(x)

###############################
#Start Slicing
x="""This is python. It is powerful"""
print(x[2:8])
#######################

#Slice from start
print(x[:3])

###########################
#Assignment
x="""Goverment polytechnic osmanpura, Chh Sambhajinagar"""
print(x[22:31])

########################
#Ssicing to the end
x="""this is python. It is very powerful."""
print(x[4:])

#Negative Indexing
#Counting from the end
s="Python"
print(s[-1])
print(s[-2])
print(s[-6])
print(s[0:5:2])
print(s[:5:2])

#
s="Powerful"
print(s[-6:-2])   #output is: "werf"

#
s="Powerful"
print(s[-2:-6])

#
'''
s = "Python"
  
  P y t h o n 
  0  1  2  3  4  5        (Positive indexing)
 -6 -5 -4 -3 -2 -1        (Negative indexing)
 '''
s= "python"
print(s[::-1])
print(s[-2:-6:-1])

##################################
#Mixing Positive and Negative Indices
s="Python"
print(s[1:-1])
print(s[-5:5])
#String
x="""this is python.It is very powerful""" 
#modify string
print(x.upper())
############
x=x.upper()
print(x.lower())

#data preparation
#remove white space,removes white space from initital to end
x="This is a Python"
x
print(x.strip())
#############
x="This is a Python"
print(x.lstrip())
##############
x="This is a Python"
print(x.rstrip())

#Replace F unction
x="Hello World"
print(x.replace("Hello","Gello"))

#Use of split which replaces whilte space/or
x="Hello_World"
print(x.split("_")) 
x="Hello World"
print(x.split(' '))
x='red-green-blue'
print(x.split('-'))
x="""This is python.It is simple to understand.Difficult to implement."""
print(x.split('.'))
