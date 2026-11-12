class vehicle:
    def __init__(self):
        pass
    def start(self):
        print("The vehicle starts")
class bike(vehicle):
    def ride(self):
        print("the boy is riding bike")
a=bike()
a.ride()
a.start()