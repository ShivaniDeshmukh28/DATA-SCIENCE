
#To get minimum value of item
sorted_dict= {'banana':40,'apple':100,'grapes':120,'mango':200}
free_item_key = min(sorted_dict, key=sorted_dict.get)
free_item_value = sorted_dict[free_item_key]
print(f"You will get the lowest priced item'{free_item_key}'({free_item_value}) for free.")

"""
min(my_dict): Returns the minimum key.
min(my_dict.values()): Returns the minimum value.
min(my_dict, key=my_dict.get): Returns the key corresponding 
to the minimum value
"""
sorted_dict= {"banana":40,'apple':100,'grapes':120,'mango':200}
free_item_key = max(sorted_dict, key=sorted_dict.get)
free_item_value = sorted_dict[free_item_key]
print(f"You will get the highest priced item'{free_item_key}' ({free_item_value}) for free.")

###########################################################################################################
#Sorting in ascending order
sorted_by_values_asce = dict(sorted(sorted_dict.items(),
                                    key=lambda item: item[1]))
print(sorted_by_values_asce)
..............................................................
#Sorting in descending order
sorted_by_values_desc = dict(sorted(sorted_dict.items(),
                                    key=lambda item: item[1],reverse=True))
print(sorted_by_values_desc)

#############################################################
#Summing values of dictionary
dict1 ={'apple':'100','grapes':'120','mango':'200','banana':'40'}
total=0
for value in dict1.values():
    total=total+int(value)
print(total)

#######################################################
#Possibility of an error
#Restart the python kernel
dict1 = {'apple':'100','grapes':'120','mango':'200','banana':'40'}
#Convert values to integers and sum them up
total_sum = sum(int(value) for value in dict1.values())
print(total_sum)

#Concatenation of dictionary by using |(pipe operator)
dict1={1: 10,2: 20}
dict2={3: 30,4: 40}
dict3={5: 50,6: 60}
dict1.update(dict2)
print(dict1)
dict1=dict1|dict3
print(dict1)

######################################
#Write a program to check if a given key is already exists
dict1={'a':20,'b':30}
print('a' in dict1)
print('b' not in dict1)
print('r' in dict1)
# in is membership operator
#################################
#continue : with the continue statement we can stop the current iteration of the
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
       continue
    print(x)





###############################
###############################
#function without argument
def my_function():
    print("hello from a function")
my_function()

..............................................
#Function with an argument
def my_function(name):
    print("Hello"+name)
my_function("Ram")
.................................................
#Function with positional argument
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("Hello","World")
my_function("JAY","SHREE")
....................................................
#Arbitrary Arguments, args*
#If you do not know how many arguments that
#will be passed into your function,
#add a * before the parameter name 
#the function definition.
def my_function(*args):
    print(args[0]+" "+args[2])

my_function("Tapu","Sonu","Goli")
.......................................................
#Function with kwargs
def my_function(**kwargs):
    for key, value in kwargs.items():
        #print("%s == %s" % (key, value))
        print(f'{key} : {value}')
        
my_function(first_name='papalal',mid_name='Mohanlal',last_name='Goyal')
#It is not necessary
.....................................
#Function with default argument
#The following example shows how to use a default parameter value.
#If we call the function without argument,
#it uses the default value:
def my_function(country = "Norway"):
    print(" I am from " + country)
    
my_function('Dubai')
my_function("Sweden")
my_function("INDIA")
my_function() #I am from Norway
my_function("Brazil")

#######################################
#Passing a List as an Argument
#You can send any data types of argument to a function (string,number,list,set,dict)
#E.g. if you send a List as an argument, it will still be a List when it reach 
fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
        
my_function(fruits)


