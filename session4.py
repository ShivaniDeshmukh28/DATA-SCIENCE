# """write a python function that accepts a hyphen-seperated 
#sequence of colors as input and returns the colors in ahyphen-seperated sequence after sorting them alphabetically"""
input_colors = "red-blue-green-yello"
def sorted_colors(input_colors):
    string_split=input_colors.split('-')
    string_split
    sort=sorted(string_split)
    sort
    sorted_string='-'.join(sort)
    return sorted_string
sorted_alphabetic=sorted_colors(input_colors)
print(sorted_alphabetic)

###########################

#palindrome
def is_palindrome(input):
    if input=="":
        return "You entered wrong input"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False

print(is_palindrome("step on no pets"))
print(is_palindrome("pets"))
print(is_palindrome("madam"))
        
###########################################

#
x="This is python and it is very powerfull"
print(x.find("and"))

address='4/116 Gokuldham Apartment,Gajanannagar'
print(address.find('Gokuldham'))
address[6:25]

####################################
#String Concatness
x='hello'
y='world'
print(x+y)

#To add white space
print(x+" "+y)

#String Format
x=21
y="my name is SHIVANI"
print(x+y)

#It will give an error
print(f"my name is SHIVANI and my age is {21}")

##########################################
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item numper is {item_no}, its price is {price}")

##############################################
#Format function
my_order="I want {} pieces and item number is {}, its price is {}"
print(my_order.format(quantity,item_no,price))

##############################################

quantity=3
price=67
item_no=54
my_order="Iwant {0} items & its item number is {1}, its price is {2}"
print(my_order.format(quantity,item_no,price))

################################################
#Escape character
text="This is fun fair and it has got big "round rigo""
#it will show you an error
text="This is fun fair and it has got big \"round rigo\""
#text="This is fun fair and it has got big "round rigo""
print(text)

########################################
#Python boolean operator
print(10>9)
print(10<9)
print(10==10)
#########################################
a=20
b=10
if(a>b):
    print("a is greater than b")
else:
    print("b ia greater than a")
    
#Python operator
a=20
b=10
print(a==b)
#####################
a=20
b=10
print(a!=b)

##########################
#Operator precedence
#BODMAS like
"""rule is PEDMAS"""
print(3*3+3/3-3) #7  3*3=9 + 3/3=1  =10-3=7
print(4*5-8/4+5) #4*5=20 - 8/4=2 +     21
##############################
#identity operator
a=20
b=10

print(a is b) #membership operator
print(a is not b)  #membershipoperator

######################
#pyhton list
lst=["cherry","banana","apple"]
print(lst)

print(lst[0])
print(lst[2])
#list can store heterogenius data type
lst=["cherry",1,1.3]

############################
#Append (Adds an element at the end of the list)
lst=["cheery","banana","apple"]
lst.append("Mango")
print(lst)

#######################
#Clear removes all the elements from the list
lst=["cheery","banana","apple"]
lst.clear()
print(lst)

"""homework"""

lst=['pani_puri','chakli','ladu','pavbhaji']
print(lst)
lst.append("ragda")
print(lst)
lst.reverse()
print(lst)
lst.pop(2)
print(lst)
lst.sort()
print(lst)
lst.extend('dabeli')
print(lst)

#remove duplicate elements without using set
lst = [1,2,3,4,0,4,6,7,9,1,5,5,6,7,8,9]

new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
        
print(new_lst)
        
#find llargest value in list without using max()
lst=[11,2,33,4,55,6,77,8,99]
largest=-1
second=-1
for i in lst:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)








