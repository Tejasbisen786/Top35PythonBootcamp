
import random

name="Tushar Bisen"
# reverse a number or string 
number=[1,2,3,4,5,6]
number.reverse()
# print(number)

# print(type(rev))

# print(name,number)
#   Calculator Program 
def add(num1,num2):
    return num1+num2
def Sub(num1,num2):
    return num1-num2
def Mul(num1,num2):
    return num1*num2
def Div(num1,num2):
    return num1/num2

# print("Addition : ",add(20,25))
# print("Subtraction is : ",Sub(20,25))
# print("Multiplication is : ",Mul(20,25))
# print("Division is : " ,Div(20,25))


# lambda function 

sum=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b

print(div(23,56))

# if age >18= | campus | not eligible for campus 

# age=int(input("Enter Your Age : "))

# if(age>=18):
#     print("eligible For Vote")
# else:
#     print("Not Eligible For Vote")


# checkAge= lambda age:age>=18
# print(checkAge(18))

# Random Value Generator 

# randomValue=random.random()
# print(randomValue)

# ** Generate Hex Value**
Hexval='1234567890ABCDEF'
ranval=random.choice(Hexval)
print(ranval)