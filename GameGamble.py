import time
import random
import sys

def Num_dice():
    while True:
        num_of_dice=int(input("\nChoose the number of dices you want to roll.\n minimum: 2, maximum: 6 \n"))
        if num_of_dice in range(2,7):
            return num_of_dice
        else:
            print("\nError Occured! Choose a number betweeen 2-6\n")

def Name():
    new = input("Enter your username to continue. Enter 1 if you are new: ")
    # Read the file and check if the username already exists
    with open("file.txt", "r") as fr:
        old_users = fr.read().splitlines()
    
    if new == "1":
        while True:
            user = input("Enter your new username: ")
            
            if user in old_users:
                print("Username already exists! Try again\n")
            else:
                print("Welcome new user. You have been given 50,000 ggc to begin with")
                # Append the new username to the file
                with open("file.txt", "a") as fw:
                    fw.write(f"{user}\n")
                with open("Score.txt", "a") as Sw:
                    Sw.write(f"50000\n")
                return user
    elif new in old_users:
        return new
    else:
        print("username do not found!! Try again")
        sys.exit()

def current_score(username):
    with open("file.txt","r") as fr:
        content=fr.read()
        names=content.splitlines()
    n=0
    for name in names:
        if name==username:
            n+=1
            break
        n+=1
    with open("score.txt","r") as Sr:
        scores=Sr.readlines()
    i=1
    for score in scores:
        if i==n:
            return score
        i+=1
    
def luck(number_of_dice):
    luck=list()
    for i in range(0,number_of_dice):
        luck.append(random.randint(1,6))
    return luck
def Rolling_dice(list):
    dice_sides={
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    }
    for num in list:
        for line in dice_sides.get(num, ["Invalid number"]):
            print(line)
    print("done")

def result(dice_list):
    return all(x == dice_list[0] for x in dice_list)


def UpdateScore(username,current_score,result,list,gamble,new_score):
    if result:
        new=gamble * (6**(len(list) - 1))
        UpdatedScore=current_score+new
        with open("file.txt","r") as fr:
            content=fr.read()
            names=content.splitlines()
        n=0
        for name in names:
            if name==username:
                n=n+1
                break
            n+=1
        with open("score.txt","r") as Sr:
            scores=Sr.readlines()
        scores[n-1]=str(str(UpdatedScore))+'\n'
        with open("Score.txt","w") as Sw:
            Sw.write("".join(scores))
        return UpdatedScore
    return new_score

def Money_left_after_gambling(gamble_amount,username,current_score):
    with open("file.txt","r") as fr:
        content=fr.read()
        names=content.splitlines()
    n=0
    for name in names:
        if name==username:
            n+=1
            break
        n+=1
    with open("score.txt","r") as Sr:
        scores=Sr.readlines()
    scores[n-1]=str(current_score-gamble_amount)+'\n'
    with open("Score.txt","w") as Sw:
        Sw.write("".join(scores))
    return current_score-gamble_amount


print("This is Gamble Game.\nFollowing are the rules of the game:\nGame Rules:\n- Player will choose the number of dice he/she wants to roll. 6 is the maximum and 2 is the minimum number.\n- If same face comes in all dices player wins big price.\n- Higer the number of dices lower the chance of success but higher the price.\n- Player will get 50,000 GGC initially. If he wins he will get 6^x times of coins he gambled. x=(number of dices)-1. If player looses he will lost all the GGC.\n- Minimum Gamble a player can play is 1000 GGC.\n- No limit to maximum Gamle amount.\n- GGC: Gamble Game Coins(Rs. 1 = 1000 ggc apx)")
print("If you understand the risk involved and still want to continue click 'yes' else 'no' to exit.")
time.sleep(1)
agree=int(input("\nEnter 1 for yes 0 for no "))
if agree==0:
    print("\nYou have successfully exited the game ")
    SystemExit(1)
else:
    print("\nWelcome to the game!\n")

time.sleep(1)
user=Name()
print(f"Your usernamre: {user}")
current_score=int(current_score(user))
print(f"Your total ggc currently is {current_score}")
gamble_amount=0
while True:
    gamble=int(input("Enter the amount you want to gamble: "))
    if gamble>current_score:
        print("Gamble amount exceeds your current ggc vault amount. Try again!")
    elif gamble<1000:
        print("Gamble amount must be higher than 1000")
    else:
        gamble_amount=gamble
        break

time.sleep(1)
num=Num_dice()
print(f"Your choice is {num}")
new_score=Money_left_after_gambling(gamble_amount,user,current_score)
print(f"{new_score} left in your ggc vault")
print(f"\nRolling the dices...")

dice_roll=luck(num)
time.sleep(3)
Rolling_dice(dice_roll)
result=result(dice_roll)

update=UpdateScore(user,current_score,result,dice_roll,gamble_amount,new_score)
print(f"Your ggc core have been updated to: {update}")