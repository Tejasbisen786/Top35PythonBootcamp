# Creating a Dictionary 
new={"name":"tejas","surname":"bisen"}
# print(new)

my_dict={
    "name":"Tejas",
    "userName":123,  # Duplicated value will overite existing values
    "userName":123,  # Duplicates Not Allowed Same key can not duplicated

    "isLoggedin":"true",
    "age":18,
   "city":"Gondia"
}
# print(my_dict.get("age"))
# print(my_dict)
# for x in my_dict:
#     print(my_dict)


# car={
#     "brand":"Audi",
#     "electric":False, # Boolean
#     "year":1953, # Int
#     "colors":["red","black","white"]  # List
# }

# print(car["brand"])

# print(car.get("year"))  # Returning the value of the given key which pass as parameter


# print(car.keys()) # returning the keys in the dictonary 
# print(car.values())  # returning the values in the dictionary

# print(car.items())  both return value but converted into list 

# Looping using 

car={
    "brand":"Audi",
    "electric":False, # Boolean
    "year":1953, # Int
    "colors":["red","black","white"]  # List
}

# y=list(car)
# print(y)

# Keys 
# print("Priting Keys: ")
# for x in car:
#   print(x)
# #  values
# print("\n")
# print("Priting Values: ")

# for x in car:
#   print(car[x])

# print("Priting Keys: ")
# for x in car.keys():
#   print(x)
# #  values
# print("\n")
# print("Priting Values: ")

# for x in car.values():
#   print(x)

# for x , y in car.items():
#   print(x, ':' , y)

# car.fromkeys("year")
