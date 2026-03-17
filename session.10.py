# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 14:50:41 2025

@author: shiva
"""
#Leap year
year='n'
def is_leap(n):
    if (n%4==0 and n%100!=0)or(n%400==0):
        print(f'{n} is leap year')
    else:
        print(f'{n} is not leap year')
is_leap(1900)

###############################################
#Input a score
score=int(input('Enter the score:'))
if(score<400 or score>850):   #when input is out of range
    print("Invalid")
else:
    if 400<=score<600:
        print("General")
    elif 600<=score<800:
        print("Delux")
    else:
        print("Premium")
        
###############################################       
#Reverse digit of a number
num=int(input("Enter the number:"))
while(num!=0):
    digit=num%10    #Last digit
    print(digit,end=" ")   #Print it
    num=num//10    #Remove the last digit      
        ..........................................
        
#
num=input("Enter a number:")
rev_num=num[::-1]
for digit in rev_num:
    print(digit,end=' ')
    
#############################
#Sum of even numbers in the list
lst=[3,5,7,6,8]
total=0
for i in range(len(lst)):
    if lst[i]%2==0:
        total=total+lst[i]
print(total) 
#############################
#To add digits of given number
num=int(input('Enter the number:')) 
total=0
while(num!=0):
    digit=num%10
    total=total+digit
    num=num//10
total   

################################
#Sum the digit if they are in 3,6 and 9
num=int(input("Enter the number:"))
total=0
while(num!=0):
    digit=num%10
    if digit in (3,6,9):
        total=total+digit
    num=num//10
total


#Sum of all even numbers in list




#Find sum of positive and negative numbers
lst=[10,20,-9,-3,2]
p_total=0
n_total=0
for i in lst:
    if i<0:
        n_total=n_total+i
    elif i>0:
        p_total=p_total+i
print(p_total)
print(n_total)    

#Reverse elements in the list
lst=[3,5,7,6,8]
# len(lst)=5,5-1=4 4 to 0(-1 means incluse 0 ) in step of -1
for i in range(len(lst) -1,-1,-1):
    print(lst[i],end=' ')   #printing index value
    
##############################  
#to find mini peak number
lst=[1,3,2,5,4]
for i in range (1,len(lst)-1):
    if lst[i-1]<lst[i]>lst[i+1]:
        print(lst[i])
###############################
#It finds the maximum and minimum elements in a list
#(Without using Python's built-in function max() or min() functions.)
lst=[13,4,6,8,9]
max_result=lst[0]
min_result=lst[0]
for i in range(1,len(lst)):
    if lst[i]>max_result:
        max_result=lst[i]
    elif lst[i]<min_result:
        min_result=lst[i]
        
print(max_result)
print(min_result)








    
def