#1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
number =int(input('Enter a number : '))
new_num = number // 10
print(new_num)

#2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
number =int(input('Enter a number : '))
new_num = number%10
print(new_num)

#3. Write a python script to swap data of two variables
num_1 = int(input('Enter a number 1 : '))
num_2 = int(input('Enter a number 2 : '))
num_1,num_2 = num_2,num_1
print("after swapeing  number 1 is {},number 2 is {} ".format(num_1,num_2 ))

#4. Write a python script to find x power y, where values of x and y are given by user
x = float(input('Enter x value: '))
y = float(input('Enter y value: '))
z = x**y
print("x power y is ",z)

#5. Write a python script which takes a three digit number from the user and displays only its first digit.
num_1 = int(input('Enter a three digit number : '))
new_num = num_1 // 10
print("first digit is ",new_num)

#6. Write a python script which takes a three digit number from the user and displays only its middle digit.
num_1 = int(input('Enter a three digit number : '))
new_num = num_1%100
num = new_num // 10
print("middle digit is ",num)

#7. Write a python script which takes a three digit number from the user and displays only its last digit.
number =int(input('Enter a three digit number : '))
new_num = number%10
print(new_num)
print("last digit is ",new_num)

#8. Write a python script to use IN operator to display the data present in the list
num_1 = int(input('Enter a number 1 : '))
number_list =[1,2,3,30,4,5,6,7]
print(num_1 in number_list)

#9. Write a python script to use NOT IN operator to display the data not present in list
num_1 = int(input('Enter a number 1 : '))
number_list =[1,2,3,30,4,5,6,7]
print(num_1 not in number_list)

#10. Write a python script to use IS operator to display if both variables are the same object or not?
num_1 = int(input('Enter a number 1 : '))
num_2 = int(input('Enter a number 2 : '))
print(num_1 is num_2)
