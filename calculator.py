print("calculator")
print("enter the operator:+,-,*,/")
op=input("enter the operator:")
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
if op=="+":
    result=num1+num2
    print(f"result:{num1}+{num2}={result}")
elif op=="-":
    result=num1-num2
    print(f"result:{num1}-{num2}={result}")
elif op=="*":
    result=num1*num2
    print(f"result:{num1}*{num2}={result}")
elif op=="/":
    if num2!=0:
        result=num1/num2
        print(f"result:{num1}/{num2}={result}")
    else:
        print("error:division by zero not allowed")
else:
    print("invalid operator")
