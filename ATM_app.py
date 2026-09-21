import random
old_otp = random.randint(1000,9999)
print(old_otp)
attemps=3
login=False
while attemps > 0:
    new_otp=int(input("enter your received OTP "))
    if old_otp != new_otp:
        attemps-=1
        print(f'wrong otp. {attemps} attemps left')
    else:
        print("login Successful")
        login=True
        break
else:
    print("you are blocked due to many failure attemps")

class Account:
    def __init__(self):
        self.balance=1000
    
    def deposit(self,amount):
    
        if amount >0:
            print("amount deposited succesfully")
            self.balance+=amount
        
    def withdrawl(self,amount):
        
        if amount <= self.balance:
            print("Amount withdrawl succesfully")
            self.balance-=amount    
        else:
            print("Insufficient Balance")
            
    def get_balance(self):
        print(f'balance amount:{self.balance}')
    def exit(self):
        print("Thankyou for using Our Services")
        
if login:
    a=Account()
    while True:
        print("choose your option")
        print("1: for deposit")
        print("2: for withdrawl")
        print("3: for balance checking")
        print("4:Exit")
        opt=int(input("enter your choice number"))
   
        if opt==1:
            amount=int(input("enter amount: "))
            if amount <= 0:
                print("Invalid amount")
            else:
                a.deposit(amount)
        elif opt==2:
            amount=int(input("enter amount: "))
            if amount <=0:
                print("Invalid Amount")
            else:
                a.withdrawl(amount)
        elif opt==3:
            a.get_balance()
        elif opt==4:
            a.exit()
            break
        else:       
            print("Invalid Choice")
else:
    print("you can't access out ATM services")

    