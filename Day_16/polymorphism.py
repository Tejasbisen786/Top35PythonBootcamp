# ****Eror Handling *******

x=5
y=0
try:
    z=x/y
except ZeroDivisionError:
    print(" Code Cant run")
finally:
    print("All Done")

    # except Exception as e 
    #  print("error captured",e)