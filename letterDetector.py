vowels_list = ["a", "e", "i", "o", "u"]
consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", 
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


line_inp = int(input("How many lines will there be? "))

num_vow = 0
num_cons = 0

for line in range(line_inp):
    lines = input()
    lower_lines = lines.lower() #to take lower because our list contains only lowerrcases
    for letter in lower_lines:
        if letter in vowels_list:
            num_vow+=1
        elif letter in consonant_list:
            num_cons+=1
            
print(num_vow)
print(num_cons)
