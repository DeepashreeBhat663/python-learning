def addstudent():
        name=input("enter a name:")
        grade=input("enter a grade:")
        student[name]=grade
        print("element added successfully")
def deletestudent():
    key=input("enter a record to be deleted:")
    if key in student:
         student.del("key")
         print("entered element is deleted succesfully")
    
def searchstudent():
    a=print("enter the key to be searched")
    if a in student:
         print(student.get("a"))
         print()
    
def displaystudent():
    if not student:
        print("dictionary is empty")
    else:
        print("student records:")
        print(student)





student={}
while True:
    print("-----MENU-----")
    print("1.ADD")
    print("2.DELETE")
    print("3.SEARCH")
    print("4.DISPLAY")
    print("5.EXIT")
    choice=int(input("enter a choice:"))
    if choice==1:
           addstudent()     
    elif choice==2:
        deletestudent()
        
    elif choice==3:
        searchstudent()
    elif choice==4:
        displaystudent()
        
    else:
        exit()
        
        