file=open("friends.txt","w")
for i in range(6):
    name=input("enter a name:")
    file.write(f"{name}\n")
file.close()
    