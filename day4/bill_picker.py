import random
names = input("enter everybodys name seprated by comma ,- ").split(", ")
print(f"{random.choice(names)} will pay the bill{names}")
