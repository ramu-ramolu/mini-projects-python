import random
old_otp=random.randint(100000,999999)
print(f'your otp is: {old_otp}')
attempts=4
while attempts> 0:
    new_otp= int(input("enter your otp:"))
    if old_otp != new_otp:
        attempts -= 1
        print(f"Login failed. Attempts left: {attempts}")
    else:
        print("Login successful")
        break
if attempts==0:
    print("you are blocked due to many wrong attempts")

        