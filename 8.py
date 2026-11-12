try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)

except ZeroDivisionError as e:
    print(f"error:{e}.PLease enter valid number..")
    b=int(input("enter b:"))
    print(a/b)
except ValueError as e:
    print(f"error:{e}.PLease enter valid number..")
    
    
else:
    
    print("no error")
finally:
    print("program finished")