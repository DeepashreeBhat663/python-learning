class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def check_balance(self):
        print(f"account balance is {self.__balance}")
    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print(f"after deposit, balance is {self.__balance}")
    def withdrawal(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            print(f"after withdrawal, balance is {self.__balance}")      
        else:
            print("insufficient balance")

            
aa=BankAccount(100001,8000)
aa.check_balance()
aa.deposit(1000)
aa.withdrawal(20000)
# Direct access to private attributes will raise AttributeError
#print(aa.__balance)
#print(aa.__account_number)