#1. Write a python script to convert a number into str type.
a = 100
print(type(str(a)))
#2. Write a python script to print Unicode of the character ‘m’
print(ord('m'))
#3. Write a python script to print character representation of a given unicode 100.
print(chr(100))
#4. Write a python script to print any number and its binary equivalent
a = 50
print(a ,"its binary equivalent" + " is "+ bin(a))
#5. Write a python script to print any number and its octal equivalent.
b = 50
print(b ,"its octal equivalent" + " is "+ oct(b))
#6. Write a python script to print any number and its hexadecimal equivalent.
c = 50
print(c ,"its hexadecimal equivalent" + " is "+ hex(c))
#7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
d = 0b1100101
print("decimal of d is ",int(d))
#8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
e = 0x2F
print("octal of e is ",oct(d))
#9. Write a python script to store an octal number 125 in a variable and print it in binary format.
f = 0o125
print("binary of f is ",bin(d))
#10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.
g = oct(25)
h = hex(39)
add = 25 + 39
print("binary of added value is ",bin(add))

