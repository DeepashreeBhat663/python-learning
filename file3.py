count=0
file=open("friends.txt",'r')
for line in file:
    count+=1
print(f"the no.of friends listed are:{count}")
file.close()