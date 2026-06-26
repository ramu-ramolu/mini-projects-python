balance=1000
while True:
    print("choose your option")
    print("1: for deposit")
    print("2: for withdrawl")
    print("3: for balance checking")
    print("4.Exit")
    opt=int(input("enter your choice number"))
    if opt==1:
        deposit=int(input("enter your deposit amount:"))
        if deposit>0:
            print("amount deposited successfully")
            balance+=deposit
            print(f'Now your balance amount is : {balance}')
    elif opt==2:
        withdrawl=int(input("enter your withdrawl amount"))
        if withdrawl<=balance:
            print("withdrwal successfull")
            balance-=withdrawl
            print(f'Now your balance amount is : {balance}')
        else:
            print(f'your balance amount is {balance}. and your withdrawl amount is less than your balance amount')
    elif opt==3:
        print(f'your balance amount is: {balance}')
    elif opt==4:
        print("Thankyou for using our services")
        break
else:
        print("please enter the correct option")
    
        
        