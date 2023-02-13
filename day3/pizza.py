print("Welcome to pizza shop. Please describe your order-")
size = input("what size of pizza do you want? S,M,L ")
pepproni = input("do you want peproni? Y,N ")
cheese = input("do you want extra cheese? Y,N ")
bill=0
if size == 'S':
    bill +=12
elif size == 'M':
    bill +=20
elif size == 'L':
    bill +=25
if pepproni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill +=3
if cheese == 'Y':
    bill += 1
print(f"Your final bill is {bill}")
