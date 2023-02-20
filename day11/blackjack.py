import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = int(random.choice(cards))
    return card
def calculate_score(alist):
    if sum(alist) == 21:
        return 0
    elif sum(alist)>21 and 11 in alist:
        alist.remove(11)
        alist.append(1)
    return sum(alist)
def compare():
    if(score_u == score_c):
        print("Draw")
    elif(score_u ==0 or score_c>21):
        print("Player won")
    elif(score_c==0 or score_u>21):
        print("Compuer won")
    elif(score_c>score_u):
        print("COmputer won")
    else:
        print("PLayer won")

flag = True
while flag:
    print(logo)
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    score_u =calculate_score(user_cards)
    score_c = calculate_score(computer_cards)
    print(f"First card of computer is- {computer_cards[0]}")
    print(f"Your card are {user_cards}")

    while  input("do you want to pick more cards: Y/N- ")=='y':
        user_cards.append(deal_card())
        print(f"Your card are {user_cards}")
    while score_c <17:
        computer_cards.append(deal_card())
        score_c = calculate_score(computer_cards)
    score_u =calculate_score(user_cards)
    compare()
    if input("Do you want to reset the game Y/N- ") == 'n':
        flag = False
