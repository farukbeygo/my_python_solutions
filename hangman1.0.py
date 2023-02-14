import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code

word_length = len(chosen_word)
health=6
stay_game=True
guess_base = []

while (stay_game == True):
  nonletter=0
  print("\n\nyour health:" + "x"*health)
  guess = input("Guess a letter: ").lower()
  if (guess not in chosen_word):
    health-=1
  for i in range(word_length):
    if (chosen_word[i] == guess) or (chosen_word[i] in guess_base):
      print(chosen_word[i], end="")
      if (guess not in guess_base):
        guess_base.append(guess)
    else:
      print("_", end="")
      nonletter+=1
  if (health==0) or (nonletter==0):
    stay_game = False
    if health==0:
      print(f"\n\nyou lost the game, the word was {chosen_word}")
    else:
      print("\n\nyou won the game!!")
  
