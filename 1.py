from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    def message(self):
        print("Welcome to payment system")

class creditcard(payment):
    def pay(self):
        print("payed through card successfully")
class cash(payment):
    def pay(self):
            print("payed through cash successfully")
class online(payment):
     def pay(self):
                 print("payed through upi successfully")
a=creditcard()
a.pay()
b=cash()
b.pay()
c=online()
c.pay()
a.message()

