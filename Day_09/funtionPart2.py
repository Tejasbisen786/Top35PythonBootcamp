def myFucntion():
    global local_var1
    local_var1=234; # Local Variable 


globalvar1=50


# myFucntion()
# print(globalvar1)
# print(local_var1)  // this would raise eror cause scope in just inside the function 
# only and it will accesable within a function 

# to make varibale global use global varable but first declred 
# print(local_var1)

# *** Recursion ****
# a function call itself etiher directly or indirecly through another function 

def factorial(n):
    if n==0:
     return 1
    else:
       return n*factorial(n-1)
print(factorial(5))    


# logic  5*4*3*2*1