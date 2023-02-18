auction = {}
flag=True
while flag == True:
    name = input("please enter your name- ")
    amount = int(input("Please enter your bidding amount- "))
    auction[name]=amount
    conti = input("Want to add more persons? Yes, NO- ")
    if conti == "no":
        flag =False
win = int(0)
winner = ""
for x in auction:
    if win <=auction[x]:
        winner = x
        win = auction[x]
print(f"{winner} has the highest bid of {win}")
