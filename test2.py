# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 15:18:48 2025

@author: shiva
"""

#Question 5: Write a program to sum only odd digits of a number.
# Example: Input: 12345 Output: 9 (1 + 3 + 5)




#Question 2: Write a program to count the number of digits in a given number.
# Example: Input: 98765 Output: 5
lst=map(int(input("enter no ")))
total=0
for i in range(len(lst)):
    total=total+lst[i]
print(lst[i])  


      
#Question 1: Write a program to find the difference between two lists.
A = [1, 2, 3, 4, 5]
B = [3, 4, 6]
Output: Difference (A - B) = [1, 2, 5]

rows=len(A)
col=len(B[0])
result=0
for i in range(rows):
    for j in range(col):
        A[i][j]-B[i][j]
        result[i][j]=A[i][j]-B[i][j]
print(f'{result[i][j]}')


#Question 3: Write a program to find the product of all digits of a number. 
#Example: Input: 234 Output: 24

def multiplication():
    for in range(lst):
        print(i*i)
    return

multiplication=lambda x:x*x 
print(234) 

#Question 4: Write a program to check whether a number is a palindrome using digit manipulation.
# Example: Input: 1221 Output: Palindrome
x="jay"
if x[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    return
reverse("madam")
reverse=lambda x:x[::-1]
