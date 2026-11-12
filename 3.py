class shape:
    def __init__(self):
        pass
    def calculate_area(self):
        print("different shapes have different areas")
class circle(shape):
    def calculate_area(self,r):
        super().calculate_area()
        area=r*3.14*r
        print(area)
class rectangle(shape):
    def calculate_area(self,l,b):
        super().calculate_area()
        area=l*b
        print(area)
shapes=[circle(),rectangle()]
for shape in shapes:
    if isinstance(shape,circle):
        shape.calculate_area(2)
    elif isinstance(shape,rectangle):
        shape.calculate_area(2,4)

    