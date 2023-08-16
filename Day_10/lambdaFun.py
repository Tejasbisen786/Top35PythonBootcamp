
# using List Comprhension
number=[1,2,3,4,5,6]
# expression | 
squres=[x**2 for x in number]

# print(squres)

square=[x **2 for x in range(1,21)]
# print(square)

# ODD EVEN CONDTION 

evenNumber=[x for x in range(1,11) if x%2!=0]
# print(evenNumber)

evenNumber1=[]
for x in range(1,11):
    if(x%2==0):
        evenNumber1.append(x)
# print(evenNumber1)        


# x%2==0 || x%2!=0

# Python lambda

# it short the function in a one liner way 

# def sqaure(x):
#     return x**2

# square= lambda x: X**2
# print(sqaure(2))

# def hello(msg):
#     print("hello",msg)


# hello=lambda msg: print("Hello",msg)
# hello("TEjas")


# add=lambda x,y:x+y
# div=lambda x,y:x/y
# mul=lambda x,y:x*y
# sub=lambda x,y:x-y

# print(add(2,4))


# Filters 

# def myfunc(n):
#  return n
# x= lambda n :n
# x= lambda a,b:a+b
# x= map(lambda n :n,('apple','banana','Cherry'))

# for item in x:
#    print(item)

# celus=[10,29,30,40,40]

#  *************************
# fah= map(lambda c : c*9/5+32,celus)
# for item in fah:
#     print(item)


# filter work on true or false 