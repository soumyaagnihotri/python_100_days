import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l= int(input("How many letters would you like in your password?\n")) 
s = int(input(f"How many symbols would you like?\n"))
n = int(input(f"How many numbers would you like?\n"))
password = ""
pswd = []
for x in range(1,1+l):
    pswd.append(random.choice(letters))
for x in range(1,1+s):
    pswd.append(random.choice(symbols))
for x in range(1,1+n):
    pswd.append(random.choice(numbers))
random.shuffle(pswd)
for x in pswd:
    password += x
print(password)
