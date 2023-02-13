#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

len_letters = (len(letters)-1)
len_numbers = (len(numbers)-1)
len_symbols = (len(symbols)-1)



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""""
password_basic = ""

for letter in range(nr_letters):
  num = random.randint(0,len_letters)
  password_basic+=letters[num]
for letter in range(nr_numbers):
  num = random.randint(0,len_numbers)
  password_basic+=numbers[num]
for letter in range(nr_symbols):
  num = random.randint(0,len_symbols)
  password_basic+=symbols[num]
print("here is basic password:" ,password_basic)
"""""
  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
nr_total = nr_letters + nr_numbers + nr_symbols
password_hard = ""


for i in range(nr_total):
  if (nr_letters>0 and nr_numbers>0 and nr_symbols>0):
    randomness = random.randint(0,3)
    if randomness==0:
      num = random.randint(0,len_letters)
      password_hard+=letters[num]
      nr_letters-=1
    elif randomness==1:
      num = random.randint(0,len_numbers)
      password_hard+=numbers[num]
      nr_numbers-=1
    else:
      num = random.randint(0,len_symbols)
      password_hard+=symbols[num]
      nr_symbols-=1
  elif ((nr_letters>0 and nr_numbers>0) or (nr_letters>0 and nr_symbols>0) or (nr_symbols>0 and nr_numbers>0)):
    randomness = random.randint(0,2)
    if (nr_letters==0):
      if randomness==0:
        num = random.randint(0,len_numbers)
        password_hard+=numbers[num]
        nr_numbers-=1
      elif randomness==1:
        num = random.randint(0,len_symbols)
        password_hard+=symbols[num]
        nr_symbols-=1
    elif(nr_numbers==0):
      if randomness==0:
        num = random.randint(0,len_letters)
        password_hard+=letters[num]
        nr_letters-=1
      elif randomness==1:
        num = random.randint(0,len_symbols)
        password_hard+=symbols[num]
        nr_symbols-=1
    else:
      if randomness==0:
        num = random.randint(0,len_letters)
        password_hard+=letters[num]
        nr_letters-=1
      elif randomness==1:
        num = random.randint(0,len_numbers)
        password_hard+=numbers[num]
        nr_numbers-=1
  else:
    if (nr_numbers>0):
      num = random.randint(0,len_numbers)
      password_hard+=numbers[num]
      nr_numbers-=1
    elif (nr_letters>0):
      num = random.randint(0,len_letters)
      password_hard+=letters[num]
      nr_letters-=1
    else:
      num = random.randint(0,len_symbols)
      password_hard+=symbols[num]
      nr_symbols-=1
    

  
print("here is hard password:" ,password_hard)
