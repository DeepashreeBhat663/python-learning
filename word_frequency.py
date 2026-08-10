w=input("enter the words:")
l=w.split()
count={}
for word in l:
    if word in count:
        count[word]=count[word]+1
    else:
        count[word]=1
print(count)