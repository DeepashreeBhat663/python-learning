class Animal:
    pass
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
animals=[Dog(),Cat()]
for animal in animals:
    animal.sound()
