# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#display string
print('Hello World')
############################################
#Display number & its type
x=1
print(type(x))
###########################################
#Identifying datatype
age=input('Please enter your age:')
print(type(age))
print(age)
##########################################
##TYPE CASTING
#Converting string to integer
age1=int(input('Enter age:'))
print(type(age1))
print(age1)

age2=int(input('Enter no:'))
print(type(age2))
print(age2)

age=(age1 + age2)
print(type(age))
print(age)

#Floating point number
#Converting to Float
exchange_rate=1.83
print(type(exchange_rate))

int_value = 100
float_value=1.5
string_value='1.5'
float_value=float(int_value)
print('int value as a float:',float_value)

float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))
###########################################
#Complex Number
c1=1  #real no.
c2=2j #imaginery no.
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
############################################
#Boolean value
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

#string into boolean
status=bool(input('ok is it confirmed?:'))
print(status)
print(type(status))
#########################################
#Arithmetic operator
home=20
away=15
print(home + away)
print(type(home + away))

print(20*15)
print(type(20*15))

goals_for=7
goals_against=10
print(goals_for - goals_against)
print(type(goals_for - goals_against))
