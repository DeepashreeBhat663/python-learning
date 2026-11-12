file=open("marks.txt","a")
name=input("enter ur name:")
marks=int(input("enter ur marks:"))
file.write(f"{name}-{marks}")