# ****Day : 08 function *****

def addNumber(a,b):
    return a+b

sum=addNumber(18,45)
# print("Sum is:",sum)

 #reusibility Concept
sum=addNumber(13,45)
# print("Sum is:",sum)
# num=10
# i=0
# def oddEvenPrint(num):
#     while(i<=num):
#         if(i%2==0):
#             print(i)
#         else:
#             print(i)  
#         i=i+1
#     return 0    


# sum=oddEvenPrint(10)
# print(sum)




# def printMyNAme(fnames):
#     print("Hii" + fnames)

# printMyNAme("Tejas")
#     # print(res)



# def printNumberSeries(number):
#     for x in number:
#      print(x)


# res = printNumberSeries(10)
# print(res)

# def multiplication_table(number, limit):
    
#     for i in range(1, limit + 1):
#         result = number * i
#         print(f"{number} x {i} = {result}")

# multiplication_table(5, 10)
            
# def extractEmail(emial):   # Parameter
#     return emial.split("@")[0]

# print(extractEmail("tejasbisen@gmail.com"))  # Argument



# def myName(fname,lname):
#     return fname,lname
# print(myName("tejas ","Bisen"))

#**Default Parameter

# def myName(fname="Tejas"):
#     return fname
# res= myName("kodyfier")
# print(res)


# **Return Value

# def addtwo(a,b):
#     swap=addtwo
# print(addtwo(10,20))

# def makeUpperCase(myName):
#     return myName.upper()
# upper=makeUpperCase("tejasbisen")
# print(upper)

# **tuple unpacking the value with return type 
# def addtwo(a,b):
#     res1=a+b
#     res2=a-b
#     return res1 , res2

# out1,out2=addtwo(34,10)
# print(out1,out2)

# out_1,out_2 = addtwo(out1,out2)
# print(out_1,out_2)

# *****pass in function *****
def myFucntion():
    # sum=23+34
    # print(sum)
    pass
myFucntion()


def sumNum():
 sum=0
input=int(input("Enter The Number till you want sum "))
for x in range(input+1):
    sum+=x
print(sum)

sumNum()


# ** Kodyfier Team  COde Analysis

def calculate_subtotal(items):

    subtotal = sum(item['price'] * item['quantity'] for item in items)

    return subtotal

 

def apply_discount(subtotal, discount_percentage):

    discount = subtotal * discount_percentage / 100

    return subtotal - discount, discount

 

def calculate_tax(total, tax_rate):

    tax_amount = total * tax_rate / 100

    # total = total + tax_amount

    return tax_amount

 

def calculate_total(subtotal, tax_amount):

    total = subtotal + tax_amount

    return total

 

# Customer's shopping cart

cart = [

    {'item': 'Shirt', 'price': 2000.0, 'quantity': 2},

    {'item': 'Jeans', 'price': 5000.0, 'quantity': 1},

    {'item': 'Shoes', 'price': 8000.0, 'quantity': 1}

]

 

# Calculate the total cost for the customer's order

subtotal = calculate_subtotal(cart)

tax_amount = calculate_tax(subtotal, tax_rate= 5)

total_cost = calculate_total(subtotal, tax_amount)

subtotal_after_discount, discount = apply_discount(total_cost, discount_percentage=20)

 

 

# Display the result

print(f"Subtotal: {subtotal:.2f} Rs ")

print(f"Tax amount: {tax_amount:.2f} Rs ")

print(f"Total after discount: {total_cost:.2f} Rs ")

print(f"Discount Applied: {discount:.2f} Rs ")

print(f"Total cost: {subtotal_after_discount:.2f} Rs ")