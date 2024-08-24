import random as ra
while True:
    diff=int(input("Choose difficulty level from 1-10 \n"))
    if(diff<1 or diff >10):
        print("How smart you really need to be to choose a number between 1 to 10?\nDo it again")
        continue
    Ub=diff*10
    Lb=1
    Total_Chaances=3+diff
    print("You get ",Total_Chaances," total chances")
    ran_num=ra.randint(Lb,Ub)
    chance=0
    while(chance<=Total_Chaances):
        chance=chance+1
        if(chance==1):
            print("choose a number between ",Lb," to ",Ub)
        else:
            print('Try again')
        num=int(input("Choose your guess\n"))
        if(num==ran_num):
            print("You got it")
            break
        elif(num>ran_num):
            print("Guess Smaller")
        else:
            print("Guess Larger")
        if(chance>Total_Chaances):
            print("You have run out of chances. The correct number is ",ran_num,"\nBetter luck next time")