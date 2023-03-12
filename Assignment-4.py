#1. Write a python script to take your name as input from the user and then print it.
z=input("Enter your your good name :")
print(z)

#2. Write a python script to take input from the user. Input must be a number.
print(int(input("Enter a number :")))

#3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
a ,b= int(input("Enter a number :")),int(input("Enter another number to add :"))
c =a+b
print("Sum of numbers is ",c)

#4. Write a python script which takes the radius from the user and display area of a circle.
import math 
radius  = float(input("Enter the radius  of a circle to area of a circle :"))
area = math.pi * (radius**2)

#5. Write a python script to calculate the square of a number. Number is entered by the user.
number = int(input("Enter a number :"))
square =  number ** 2
print("square of  entered number is ",square)

#6. Write a python script to calculate the area of Triangle. Number is entered by the user.
b = float(input("Enter a base  :"))
h = float(input("Enter a height :"))
area = (b * h)/2
print(area)

#7. Write a python script to calculate average of three numbers, entered by the user
num_1 = float(input("Enter a number :"))
num_2= float(input("Enter a 2nd number :"))
num_3 = float(input("Enter a 3rd number :"))
i = (num_1+num_2+num_3)/3
print(i)

#8. Write a python script to calculate simple interest
p = float(input("Enter Principal amout :"))
r = float(input("Enter intrest rate :"))
t = float(input("Enter number of years :"))
si = (p *r*t)/100
print(si)

#9. Write a python script to calculate the volume of a cuboid.
l = float(input("Enter Length :"))
w = float(input("Enter Width :"))
h = float(input("Enter Height :"))
v = l*w*h
print(v)

#10. Write a python script to calculate area of a rectangle
l = float(input("Enter Length :"))
w = float(input("Enter Width :"))
area = l * w
print(area)
