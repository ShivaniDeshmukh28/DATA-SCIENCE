#Dictionary
car = {
       "Brand":"BMW",
       "Model":"Dumble 2000",
       "Year":2000
       }
x=car.keys()
print(x)
.......................
#Adding one more key and value and finding length of dictionary
car["color"]="sky-Blue"
car
x=car.keys()
print(x)
print(len(car))
..............................................
#Removing the dictionary element
car = {
       "Brand":"BMW",
       "Model":"Dumble 2000",
       "Year":2000
       }
car.pop("Model")
print(car)
.................................
#Accessing values in dictionary
car = {
"Brand":"BMW",
"Model":"Dumble 2000",
"Year":2000
       }
for x in car:
    print(car[x])
.................................................
#If you want to access both keys and values

for key, value in car.items():
    print("%s = %s" % (key,value))
    
for key, value in car.items():
    print(f"{key} : {value}")
.................................
#Copying dictionary
car={
     "Brand":"BMW",
     "Model":"Doumble 2000",
     "Year":2000
     }  
car2=car.copy()
car2  

###########################################
#Another way to make a copy is to use the built-in function
thisdict={
"Brand":"BMW",
"Model":"Doumble 2000",
"Year":2000
    }
dict1=dict(thisdict)
dict1
#########################################
#Nested dictonary
#A dictionary can contain dictionaries,
#This is called nested dictionaries.
 our_family={
     "child1":{"NAME":"RAM",
              "DoB":"28-02-2005",
              },
     "child2":{"NAME":"SHAM",
             "DoB":"03-09-2007"
             }
     }
 our_family
###################################
#Dictonary methods
#clear():Removes all elements from the car list
car={
     "Brand":"BMW",
     "Model":"Doumble 2000",
     "Year":2000
     }
car.clear()
car
##############################
#fromkey
#create a dictonary with three keys,
#all with the value 0
x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
thisdict

################################
#get() : To get the value of dictonary
car={
     "Brand":"BMW",
     "Model":"Doumble 2000",
     "Year":2000
     }
car.get("model")

############################
#item() :Return the dictonary's key-value
car={
     "Brand":"BMW",
     "Model":"Doumble 2000",
     "Year":2000
     }
car.items()
car.keys()
####################################3
#values() : display all the values of dictonary
car = {
       
       "brand":"BMW",
       "Model":"Doumble 2000",
       "Year":2000
       
       }
car.values()
##########################
#Update() : Insert an item to the dictonary
car = {
       "Brand":"BMW",
       "Model":"Doumble 2000",
       "Year":2000
       }
car.update({"Brand":"Maruti"})
car

################.........................
#Sort by key
data = {'b':2,'a':5,'c':1}
data.items()
sorted_by_keys = dict(sorted(data.items))

#Sort by value
data = {'b':2,'a':5,'c':1}
sorted_by_values= dict(sorted(data.items(), key=lambda item: item[1])
print(sorted_by_values)
##################################................
#A lambda funtion is a small
#anonymous function.
#A lambda function can take
#any number of arguments,
#but can only have one expression
def add(a):
    sum=a+10
    return sum
add(20)

add=lambda a:a+10
print(add(20))


