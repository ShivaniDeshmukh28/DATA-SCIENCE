

#Append
lst=["cheery","banana","apple"]
lst.append("Mango")
print(lst)
#####################
#copy()method
lst=["cheery","banana","apple"]
lst2=lst.copy()
print(lst2)
########################

#Count() Return the number of times the value "cheery"apprears 
lst=["cheery","banana","cheery"]
lst.count("cheery")
#######################
#for list concatenation
#extend()
lst=[1,2,3]
lst1=[4,5,6]
lst=lst+lst1
print(lst)
lst=[1,2,3]
lst1=[4,5,6]

lst.extend(lst1)
print(lst)
#####################

#insert()
lst=["cherry","cherry","banana"]
lst.insert(1,"Mango")
print(lst)
##################

#pop() Remove the elements at the specified position
lst=["cherry","cherry","banana"]
lst.pop(1,)
print(lst)
#########################
#remove() removes the item with the specified value
lst=["cheery","cherry","banana"]
lst.remove("cherry")
print(lst)
#############################################

#reverse()
lst=["cherry","banana","cherry"]
lst.reverse()
print(lst)
###############
#sort() 
#sort the list alphabetically
lst=["cherry","orange","banana"]
lst.sort()
print(lst)
################################
#sort()
words=["apple","banana","kiwi","cherry"]
sorted_words = sorted(words,key=len)
print(sorted_words)
############################

#Creating a nested list
nested_list =[[1,2,3],["a","b","c"],[True,False]]
print(nested_list)
#Accesssing elements in a nested list
nested_list[0][2]
nested_list[1][0]
###########################

#Accessing the first inner list
print(nested_list[0])
#Accessing a specific element inside a sublist
print(nested_list[1][2])
#Accesssing the last element of the last sublist
print(nested_list[-1][-1])

########################
#1)Modifying Elements in a nested list
nested_list[1][1] = "z"
print(nested_list)

#2)Iterating Over a nested list
for sublist in nested_list:
    print(sublist)
flat_list = [ sublist for sublist in nested_list]
print(flat_list)

...........................
#Using two for loops (Iterate OVER Elements)
for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")

...........................
#List Comprehension with Nested Lists
#Flattening of list
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

_______________________________________________________
#List comprehension(INTERVIEW QUESTION)
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)
..............................

#We can write same method uding list comprehenssion
lst=[num for num in range(0,20)]
print(lst)
..............................

name=["dada",'mama','kaka']
lst=[name.capitalize() for name in names ]
print(lst)
_________________________________________________________
####################################

#Adding an Entire Sublist
nested_list.append(["new","list"])
print(nested_list)
..................................

#Adding an element inside a sublist
nested_list[0].append(4)
print(nested_list)
.................................

#Removing an Element from a Sublist
nested_list[0].remove(4)
print(nested_list)
nested_list[1].remove('z')
print(nested_list)

########################################

#Tuple
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])     # tup[2] is index
.......................................

#Once a tuple is created, you cannot change its values. Tuples are immutable.
x = ("apple","kiwi","banana","cherry")
x[1]='chikoo'

#First convert into tuple
y=list(x)
y
y[1]="chikoo"
#Convert list to tuple
x=tuple(y)
print(x)
.................................

# tuple can have  different data types
x = ("apple",2,"cherry")
print(x)
.......................
#You can access tuple items by referring to the index no, inside square bracket
x = ("apple","kiwi","banana","cherry")
print(x[1])
................................
# to join two or more tuples you can use the + operator
tuple1 = ("a","b", "c")
tuple2 = (1,2,3)
tup=tuple1+tuple2
print(tup)
#############################

#Dictionary
dict1={"Brand":"Maruti","model":"2345","year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))
...................................

dict1.get("model")
dict1.keys()

......................................
car = {
       "Brand":"BMW",
       "Model":"Dumble 2000",
       "Year":2000
       }
x=car.keys()
print(x)
................................

#Adding one more key and value
car["color"]="sky-Blue"
car

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
=================================================================================
___________________________________________________________________________________

#Tuple
tup=("cherry","banana","cherry","orange")
print(tup)
print(tup[0])    #tup[0] is used for determing the element present at index

#Once a tuple is created,you can not change its value.
#tuple is immutable.
x=("apple","banana","cherry")
x[1]='kiwi'

