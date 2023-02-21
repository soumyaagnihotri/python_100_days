import random
from art import logo,won
print(logo)
print("Welcome to the gussing game \nI am thinking of a number between 1 to 100 ")
diff = input("Choose your dificulty 'Easy' or 'Hard'")
i = int(0)
num = random.randint(1,101)
if diff =="hard":
    i=5;
else:
    i=10
while i>0:
    guess=int(input("Make a guess- "))
    if(num == guess):
        print("Right guess")
        print(won)
        break
    elif(guess >num):
        print("Too high")
    else:
        print("too low")
    print("Guess again")
    i -=1
    print(f"You have {i} chances left")
    

