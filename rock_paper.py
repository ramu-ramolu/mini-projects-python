import random
choices=["rock","paper","scissors"]
while True:
    user=input("enter your choice(rock,paper,scissor)").lower()
    comp=random.choice(choices)
    print(f'you choose {user}')
    print(f'computer choose {comp}')

    if user==comp:
        print("It is a tie")

    elif(user=="rock" and comp=="scissors")or(user=="paper" and comp=="rock")or(user=="scissors" and comp=="paper"):
        print("you win")
        break
else:
    print("sry😔...you lost.computer win")