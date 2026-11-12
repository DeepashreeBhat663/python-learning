line_number=1
file=open("friends.txt",'r')
for line in file:
    if line.strip()=="shama":
        print("found",line_number)
    line_number+=1

file.close()