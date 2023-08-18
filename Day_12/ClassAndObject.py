# fundamental Of Classes And Objects 

# Class And Object Example 

class Person:
    def __init__(self,name,age):   # Constructor 
        self.name=name
        self.age=age

    def greet(self):
        print(f"I Am { self.name}")

    def describe(self):
        print(f"I am {self.age} year old")    


# Creting a object
#  object_Name = Class_Name(value1,value2) # Syantax For Creating a Object

Person1 = Person("'Tejas'",28)
Person2 = Person("Tushar",25)


#Printing a Object
# print(f"Person1 Name: {Person1.name}")
# print(f"Person1 Age: {Person1.age}")
# print(Person1.describe())
# print(Person1.greet())


print("\t")
# print(f"Person2 Name: {Person2.name}")
# print(f"Person2 Age: {Person2.age}")


# Calling a Methods
Person1.greet()
Person1.describe()



