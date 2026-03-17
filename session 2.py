#Divide operation with /
print(100/20)
print(type(100/20))   ###float would be the result

#Divide operation with //
print(100//20)
print(type(100//20))  ###integer would be the result

#Modulus operator
print('modulus division 100 %3:',100 % 3)

# power operator
a=5
b=3
print(a ** b)

#assignment operator
x=0
x+=1
print(x)

#None datatype/ value
winner=None
print('winner:',winner)
print('winner is not None:',winner is not None)
print(type(winner))
print('set winner to True')
winner = True

#flow control using if statement
#comparison operator
num=int(input('Enter a number:'))
if num>0:
   print(num)    

#Else in an IF Statement
num=int(input('Enter yet another number:'))
if num<0:
    print('its Negative')
else:
    print('its  not negative')
    
#The use of Elif
savings=float(input("Enter how much you have in savings:"))
if savings == 0:
    print("Sorry no savings")
elif savings<500:
    print("Well done")
elif savings<1000:
    print("Thats a tidy sum")
elif savings<10000:
    print("Welcome sir!")
else:
    print('Thank You')
    
#Iteration/Looping
#While loop
count=1
print('Starting')
while count<=10:
    print(count)
    count+=1

#For Loop
#Loop over a set of values in a range
print('Print out values in a range:')
for i in range (2,10):
    print(i)
    #print('Done')
#print(i)
print('Done')


################################
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for:'))
for i in range(0,16):
    if i == num:
        break
    print(i)
print('Done') 
       
###################################

#Use anonymous variable loop
for _ in range(0,10):
    print('.',end=' ')
    #print() output is in the form of vertical

###################################

#Python program to print odd Numbers in given range
start, end = 4, 19
# iterating each number in list
for num in range(start, end + 1):
    
    # Checking condition
    if num % 2 !=0:
        print(num, end = " ")
    
####################################
#Python program to print even Numbers in given range
for num in range(start, end + 1):
    
    #Checking condition
    if num % 2==0:
        print(num, end = " ")