import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

p = int(input("Please enter your choice '0 Rock','1 Paper','2 Scissors'"))
selction = ['Rock','Paper','Scissors']
print(game_images[p])
c = random.randint(0,2)
print("\n\ncomputer chose ")
print(game_images[c])
if c == p:
    print("draw")
elif p<0 or p>2:
    print("invalid input")
elif c ==0 and p == 2:
    print("You lost")
elif c ==2 and p == 0:
    print("You won")
elif c > p:
    print("you Lost")
else:
    print("You Won")
