class Bankaccount:
    def __init__(self,account_no,name,balance):
        self.__account_no=account_no
        self.name=name
        self.__balance=balance
        
    def check_balance(self):
        print(f"balance checked successfully and the balance is {self.__balance}")

    def withdraw(self,amount):

        if amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance-=amount
            print(f"now the balance is {self.__balance}")


        
    def deposit(self,amount):
        self.__balance+=amount
        print(f"now the balance is {self.__balance}")

    def account_details(self):
        print(f"Account holder:{self.name}\nAccount no:{self.__account_no}")

    def get_balance(self):
        return self.__balance
    
a=Bankaccount(23451625,"anil",15000)




class Savingsaccount(Bankaccount):
    def calculate_interest(self,rate):
        balance=self.get_balance()
        interest =balance*rate/100
        print(f"interest is {interest}")


class Currentaccount(Bankaccount):
    def calculate_interest(self,rate):
        balance=self.get_balance()
        interest =balance*rate/100
        print(f"interest is {interest}")


s=Savingsaccount(234556,"riya",9800)
c=Currentaccount(5688655,"roza",10000)







def menu():
    choice=""
    while choice!="6":
        print("___BANK MANAGEMENT SYSTEM___")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Account details")
        print("5.Calculate interest")
        print("6.exit")
        choice=input("Enter a choice:")
        print(f"your entered choice is {choice}")


        if choice=="1":
            a.check_balance()
        elif choice=="2":
            amount=int(input("Enter the amount to be deposited:"))
            a.deposit(amount)
        elif choice=="3":
            amount=int(input("Enter the amount to be withdrawed:"))
            a.withdraw(amount)
        elif choice=="4":
            a.account_details()
        elif choice=="5":


            account=input("Choose an account as savings or account: ").lower()
            
            if account=="savings":
                rate=int(input("Enter a rate:"))
                s.calculate_interest(rate)
            elif account=="current":
                rate=int(input("Enter a rate:"))
                c.calculate_interest(rate)
            else:
                print("invalid account")


        elif choice=="6":
            print("THANK YOU FOR VISITING BANK MANAGEMENT SYSTEM")
        else:
            print("invalid choice")
          
    
            
menu()

    