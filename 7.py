try:
    age=int(input("enter a age:"))
except Exception as e:
    print(f"error:{e}.PLease enter valid age..")
else:
    a=100-age
    print(f"in {a} years u will be reaching 100 years old!!")
finally:
    print("program finished")