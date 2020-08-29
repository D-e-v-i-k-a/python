1
string1 = input("Enter the first string: ")
print(string1,end = "\n")
string2 = input("Enter the second string: ")
print(string2,end = "\n")
print("Are both strings equal or not: ",end = " ")
if (string1 == string2):
  print("Equal")
else:
  print("Not Equal")

2
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = a+b
print("sum = ",sum)

3
number = int(input("Enter a number: "))
sq = number**0.5
print("square root: ",sq)



4
a = float(input("enter side one: "))
b = float(input("enter side two: "))
c = float(input("enter side three: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is ",area)


5
celsius = float(input("enter the temperature in celsius: "))
fahrenheit = (celsius*9/5)+32
print("Temperature in fahrenheit is: ",fahrenheit)


6
num = int(input("enter a number: "))
if num > 0:
  print("{0} is a positive number".format(num))
elif num == 0:
  print("{0} is zero".format(num))
else:
  print("{0} is a negative number".format(num))

7
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))
if(num1 > num2) and (num1 > num3):
  largest = num1
elif(num2 > num1) and (num2 > num3):
  largest = num2
else:
  largest = num3
print(" largest number is ",largest)
