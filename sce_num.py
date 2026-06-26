sec_num=25
attempts=5
while attempts>0:
    a=int(input('enter your number:'))
    if a==sec_num:
        print("yeah! your guess is correct")
        break
    elif a>sec_num:
        attempts -= 1
        if a-sec_num<=5:  
            print(f'your guess is wrong, you are close to the secret number.you have remaining {attempts} chnaces')
        else:
            print(f'your guess is wrong, you are far to the secret number.you have remaining {attempts} chnaces')
    elif a<sec_num:
        attempts-=1
        if sec_num-a<=5:
            print(f'your guess is wrong, you are close to the secret number.you have remaining {attempts} chnaces')
        else:
            print(f'your guess is wrong, you are far to the secret number.you have remaining {attempts} chnaces')
if attempts==0:
    print("your attempts are done.you lost the game")
    
    
            
    