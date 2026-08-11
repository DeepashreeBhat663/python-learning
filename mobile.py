class Mobile:
    def __init__(self,brand, price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"brand={self.brand} and price={self.price}")
a=Mobile("samsung",67000)
b=Mobile("vivo",76000)
a.display()
b.display()


