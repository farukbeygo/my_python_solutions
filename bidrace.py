print("Welcome to the secret auction program")
bid_dictionary = {}

stayloop = True
while stayloop:
  name = input("What is your name?")
  bid = int(input("What is your bid?"))
  bid_dictionary[name] = bid

  ask = input("Are there any other bidders? yes (Y) or no (N)")
  if ask=='N':
    stayloop = False
    name = ""
    max = -1
    
    for key in bid_dictionary:
      if bid_dictionary[key]>max:
        max = bid_dictionary[key]
        name = key

    print(f"The winner is {name} with a bid of ${max}")
