# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 14:48:32 2025

@author: shiva
"""
"""
n=8,   path="UDDDUDUU"
start: elevation = 0 (Sea level)

steps: 
    U  elevation=1
    D elevation=0
    D elevation=-1
    D elevation=-2
    U elevation=-1
    D elevation=-2
    U elevation=-1
    U elevation=o




"""
#valley count in HIKE
def valley_count(n, path):
    elevation=0     #current height from sea level (0= sea level)
    valley_count=0     #number of valleys
    
    for step in path:   # go through each step in the journey
        if step =='U':   # if the step is up
            elevation += 1    # move one step up
            if elevation == 0:   # just came back to sea level
                valley_count += 1   #completed one valley
        else:  # if the step is'D'
            elevation -= 1    # move one step down
    return valley_count

n = 8
path = "UDDDUDUU"
vc=valley_count(8,'UDDDUDUU')
print(vc)
  
###################################

#write a program to rotate list by 2
def left_rotate(lst, d):
    n = len(lst)    # Total elements in list
    d = d % n      # in case d > n (rotatetion by full cycle doesn't
                  # change the list)
    rot_text = lst[d:] + lst[:d] # Slicing & joining
    return rot_text
lst=[1,2,3,4,5]
d=2
rot_lst=left_rotate(lst,d)
print(rot_lst)

lst[d:]
lst[:d]
d=2

###################################
#matrices operations(using nested list)
mat= [
    [1, 2, 3],    # row 0
    [4, 5, 6],    # row 1
    [7, 8, 9]     # row 2
      ]
#step 1: find dimensions
rows = len(mat)    # 3 rows
cols = len(mat[0]) # 3 columns (since row 0 has 3 elements)

for i in range(rows):        # outer loop - goes row by row
    for j in range(cols):    # inner loop - goes column by column
        
        """
        outer loop i = row index (0-2)
        Inner loop j = column index (0-2)
        """
        
        print(f'Elements in [{i}][{j}] are {mat[i][j]}')
        
        #print((f'Elements in [{i}][{j}] are {mat[i][j]}')

--------------------------------------------------------------------
#Addition of thw matrix

mat=[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
  ]
mat2=[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] 
 ]
result=[
  [0, 0 ,0],
  [0, 0, 0],
  [0, 0, 0]      
        ]
 
rows=len(mat)
cols=len(mat[0])
for i in range(rows):
    for j in range(cols):
        result[i][j]=mat[i][j]+mat2[i][j]     
result

---------------------------------------------------------
#Find diagonal elements of matrix
mat1=[
      [1,2,3],
      [4,5,6],
      [7,8,9]]
rows=len(mat)
cols=len(mat[0])

for i in range(rows):
    for j in range(cols):
        if i==j:
            print(mat[i][j])
     
------------------------------------------------------------
#To decide given matrix is spares matrix or not
mat1=[
      [1,0,0],
      [0,0,2],
      [0,1,1]]
rows=len(mat)
cols=len(mat[0]) 
count=0
for i in range(rows):
    for j in range(cols):
        if mat1[i][j]==0:
            count+=1
if count>(rows*cols)/2:
    print('Sparse')
else:
    print('Not sparse')
     
     
""" HOME WORK STARTS FROM """
#WAP to rotate list by 2 at left side
def left_rotate(lst, d):
    n=len(lst)   # total no of list
    d=d%n         #if d>n then list not chnge rotate whole cycle
    rot_text=lst[d:]+lst[:d]    #do slicing then do joining
    return rot_text
lst=[1,2,3,4,5]
d=2
rot_lst=left_rotate(lst,d)
print(rot_lst)

lst[d:]
lst[:d]
d=2
#1)simple matrix operation
mat=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
     ]
rows=len(mat)
cols=len(mat[0])
for i in range(rows):
    for j in range(cols):
        print(f'Elements in [{i}][{j}] are {mat[i][j]}')
        
#Find diagonal element of matrix
mat=[
     [1,2,3],
     [4,5,6],
     [7,8,9]
     ]
rows=len(mat)
cols=len(mat[0])

for i in range(rows):
    for j in range(cols):
        if i==j:
            print('diagonal element is:',mat[i][j])
#Addition of two matrix
mat1=[
     [1,2,3],
     [4,5,6],
     [7,8,9]
     ] 
mat2=[
      [9,8,7],
      [6,5,4],
      [3,2,1] 
      ]
result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
rows=len(mat1)
cols=len(mat1[0])
for i in range(rows):
    for j in range(cols):        
        result[i][j] =mat1[i][j] + mat2[i][j]
result

#output get in row wise like(1,4,7,2,5,8,3,6,9)
mat=[
     [1,2,3],
     [4,5,6],
     [7,8,9]
     ]
rows=len(mat)
cols=len(mat[0])

for j in range(cols):
    for i in range(rows):
        print(f' Elements in [{i}][{j}] are {mat[i][j]}')