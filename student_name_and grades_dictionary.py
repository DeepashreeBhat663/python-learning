def addstudent():
        name=input("enter a name:").lower()
        grade=input("enter a grade:")
        student[name]=grade
        print("element added successfully")



def deletestudent():
    key=input("enter a record to be deleted:")
    if key.lower() in student:
         student.pop(key.lower())
         print("deleted record successfully")
    else:
         print("invalid input")
   
         


    
def searchstudent():
    a=input("enter the key to be searched:")
    if a.lower() in student:
             print(student.get(a.lower()))
    else:
        print("invalid input")
    


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
    elif choice==5:
         print("EXITING")
         break
        
    else:
        print("invalid choice")
       
        
        