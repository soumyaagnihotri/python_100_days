import random
from hangman_art import stages,logo
import hangman_words
lives = 6
world_list = hangman_words.word_list
print(logo)
choosen_word = random.choice(world_list)
print(choosen_word)
space = []

for x in choosen_word:
    space += '_'
while '_' in space and lives>0:
    guess = input("Choose a letter ").lower()
    for i in range(len(choosen_word)):
        
        if choosen_word[i] == guess:
            space[i] = guess
            

    if  guess not in space:  
        lives -= 1
        print(stages[lives])
    print(space)
if lives == 0:
    print("You Lost")
else:
    print("You won")