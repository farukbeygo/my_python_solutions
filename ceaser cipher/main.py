from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#encrypt function
def encrypt(cryp, code):
  crypted = ""
  for char in cryp:
    if char in alphabet:
      place = alphabet.index(char)
      crypted+=(alphabet[(place+code)%26])
    else:
      crypted+=(char)
  return crypted

#decrypt function
def decrypt(cryp, code):
  encrypted = ""
  for char in cryp:
    if char in alphabet:
      place = alphabet.index(char)
      encrypted+=(alphabet[(place-code)%26])
    else:
      encrypted+=(char)
  return encrypted


print(logo)
stay_loop = True
while stay_loop:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction=="encode":
    print(f"Here is your encoded result: {encrypt(text, shift)}")
    loop = input("Do you want do anything else? yes ('Y'), no ('N')")
    if loop=='N':
      stay_loop = False
  else:
    print(f"Here is you decoded result: {decrypt(text, shift)}")
    loop = input("Do you want do anything else? yes ('Y'), no ('N')")
    if loop=='N':
      stay_loop = False