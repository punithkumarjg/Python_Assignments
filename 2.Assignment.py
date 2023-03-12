#1. Write a python script to add comments and print “Learning Python” on screen.
#Learning Python (single line comments) or
''' Learning Python'''
#2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.
''' Learning Python'''
name = 'PUNITH'
age = 23
qualification = 'xyz'
years_of_experience = 2
print(name,age,qualification,years_of_experience,sep ='\n')
#3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
a,b,c,d,e = 35,True,"MySirG",5.46,3+4j 
print("Type of a is ",type(a))
print("Type of b is ",type(b))
print("Type of c is ",type(c))
print("Type of d is ",type(d))
print("Type of e is ",type(e))
#4. Write a python script to print the id of two variables containing the same integer values.
x = 10
y = 10
print(id(x))
print(id(y))
#5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
a,b,c,d,e = 35,True,"MySirG",5.46,3+4j 
print(' a is {} ,type of this is{} ,and id of this is  {}'.format(a, type(a),id(a)))
print(' b is {} ,type of this is{} ,and id of this is  {}'.format(b, type(b),id(b)))
print(' c is {} ,type of this is{} ,and id of this is  {}'.format(c, type(c),id(c)))
print(' d is {} ,type of this is{} ,and id of this is  {}'.format(d, type(d),id(d)))
print(' e is {} ,type of this is{} ,and id of this is  {}'.format(e, type(e),id(e)))
#6. Write a python script to print all the keywords
import keyword
print(keyword.kwlist)
#7. On Python shell use help() function and display the list of keywords
help()
keywords
#8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py
a=100 #in A1 file 
import A1 
print(A1.a)
#9. Name the keywords, used as data in the Python script.
True ,False ,None 
#10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)
from datetime import datetime 
datetime = datetime.today().strftime("%d-%m-%Y and %I:%M %p")
