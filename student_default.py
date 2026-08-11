class Student:
    def __init__(self,name="unknown",marks=0):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"name={self.name} and marks={self.marks}")
s1=Student("aaa",56)
s2=Student("bbb",89)
s3=Student(marks=99)
s1.display_info()
s2.display_info()
s3.display_info()