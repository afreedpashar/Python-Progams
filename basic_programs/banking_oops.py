
import sys
class Customer:
    """Customer class with bank operations"""
    bankname = 'National Bank'

    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Balance after deposit is : " ,self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds....cannot process this transaction")
            sys.exit()
        self.balance = self.balance-amount
        print("Balance after successfull withdraw ",self.balance)

print("Welcome to ", Customer.bankname)
name = input("Please anter your name : ")
c = Customer(name)
while True:
    print('d-Deposit \nw-Withdraw\ne-Exit')
    options = input("Enter the valid optons: ")
    if options == 'd' or options == 'D':
        amount = int(input("Enter the amount you want to deposit: "))
        c.deposit(amount)
    elif  options == 'w' or options=='W':
        amount=int(input("Enter the amount that you want to withdraw: "))
        c.withdraw(amount)
    elif  options=='e' or options == 'E':
        print("Thank you for banking with us")
        sys.exit()
    else:
        print("you have entered invalid options....please enter valid options")