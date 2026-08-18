class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"the student name is {self.name} and her marks is {self.marks}")
class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks=marks
student1=Student("Riya",99)
student1.display()
