# class baseclass:

#  class DerivedClass(baseclass):
  

#Attribute Inheritance:
# method Constructor 
# Method Cnstructor 
class Animal:
   def __init__(self,name,props):
     self.name=name
     self.props=props

   def speak(self):
    return "Animal Speaks"
class Dog(Animal):
    def speak(self):
     return "Dog Barks"
class Cat(Animal):
  def speak(self,props,name):
    self.name=name
    super.__init__.props=props
    return "Cat Meows"

animal = Animal("Tushar","Playing")
print(animal.speak())
print(animal.props)


cat = Cat("Tejas","Writing")
print(cat.props)







class Vehicle:

    def __init__(self, brand, model):

        self.brand = brand

        self.model = model

 

    def get_info(self):

        return f"{self.brand} {self.model}"

 

class Car(Vehicle):

    def __init__(self, brand, model, color):

        super().__init__(brand, model)

        self.color = color

 

    def get_info(self):

        return f"{self.color} {self.brand} {self.model} car"

 

class Bike(Vehicle):

    def __init__(self, brand, model, type):

        super().__init__(brand, model)

        self.type = type

 

    def get_info(self):

        return f"{self.brand} {self.model} {self.type} bike"

 

# Creating instances of the child classes

car = Car("Toyota", "Camry", "Blue")

bike = Bike("Honda", "CBR500R", "Sport")

 

# Calling methods on instances

print(car.get_info())

print(bike.get_info())



  