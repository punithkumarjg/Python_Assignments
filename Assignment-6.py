#1. Write a python script to check whether a given number is positive or non-positive
number = int(input("enter a number : "))
print(number," number is positive ") if number >0 else print(number," number is non-positive ")

#2. Write a python script to check whether a given number is divisible by 5 or not
number = int(input("enter a number : "))
print(number," number is divisible by 5 ") if number%5 ==0 else print(number," number is not divisible by 5 ")

#3. Write a python script to check whether a given number is even or odd
number = int(input("enter a number : "))
print(number," number is even ") if number%2 ==0 else print(number," number is odd ")            

#4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
a=int(input("enter a number  : "))
b =int(input("enter a number : "))
print(a,"  is greater ") if  a > b  else print(b,"  is greater")

#5. Write a python script to print two given words in dictionary order
a=(input("enter word: "))
b =(input("enter word : "))
print(b,a) if  a > b  else print(a,b) 

#6. Write a python script to check whether a given number is a three digit number or not.
num=int(input("enter a number to check whether a number is a three digit number or not : "))
print("number is a three digit number ") if int(num/1000) == 0 else print("number is not a three digit number ")
# or
num=int(input("enter a number to check whether a number is a three digit number or not : "))
print("number is a three digit number ") if 99<num<1000 else print("number is not a three digit number ")

#7. Write a python script to check whether a given number is positive, negative or zero.
number = int(input("enter a number : "))
if number > 0:
   print("number is positive ")
elif number ==0:
     print("number is Zero ")
else:
    print("number is negative ")

#8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
print("enter value of coefficient a,b,c of quadratic equation")
a,b,c = int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("Real and distinct roots")
elif d == 0:
     print("real & equal roots")
else :
    print("imaginary roots")

#9. Write a python script to check whether a given year is a leap year or not.
year = int(input("enter year number : "))
if year%400 == 0 or year%100 == 0 or year%4  == 0:
    print("year is a leap year")
else :
    print("not a leap year")

#10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
print("enter three numbers")
a,b,c = int(input()),int(input()),int(input())
print((a if a>c else c) if a>b else(b if b>c else c))

#11. Write a python script to take the month value in numeric format and display the number of days in it.
month = int(input("enter month number :"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 day")
elif month == 2 :
    print("29 or 28 days")
else :
    print("enter valid month number")
#12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
x = complex(input("enter a complex number :"))
print(x.real) if x.real>x.imag else print(x.imag)
