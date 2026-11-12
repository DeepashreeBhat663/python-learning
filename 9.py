list=[]
n=int(input("enter a number of elements:"))
for i in range(n):
    num=int(input("enter a number:"))
    list.append(num)
print(list)

def addition(x):
    return sum(x)
def average(x):
    return s/len(x)
s=addition(list)
a=average(list)
print(s)
print(a)