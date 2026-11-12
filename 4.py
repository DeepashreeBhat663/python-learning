class bankaccount :
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        self.__balance=balance
a=bankaccount(45000)
print(a.get_balance())
a.set_balance(46000)
print(a.get_balance())
