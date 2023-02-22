import random
from art import logo,vs
from game_data import data

import os
os.system('cls')
print(logo)
condition =True
score =0
a = random.choice(data)
b= random.choice(data)
while condition:
    a=b
    b= random.choice(data)
    os.system('cls')
    print(logo)
    print(a)
    print(vs)
    print (b)
    guess=input("Who has more followers. Type 'A' or 'B'-")
    if ((guess=='a' and a["follower_count"]>=b["follower_count"]) or (guess == 'b' and a["follower_count"]<=b["follower_count"])):
        score +=1
        print(f"You're correct, current score is {score}")
    else:
        print("Your guess is worng")
        condition = False


