alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text,shift):
    cipher = ""
    for i in text:
        ind = alphabet.index(i)
        new_ind = alphabet[(ind+shift)%26]
        cipher += new_ind
    print(cipher)
def decrypt(text,shift):
    cipher = ""
    for i in text:
        ind = alphabet.index(i)
        new_ind = alphabet[(ind-shift)%26]
        cipher += new_ind
    print(cipher)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)
