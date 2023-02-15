from art import logo

print(logo)
stayloop = True

def addition(n1, n2):
  return n1+n2

def substraction(n1, n2):
  return n1-n2

def multiplication(n1, n2):
  return n1*n2

def division(n1, n2):
  return n1/n2

operation = {
  "+":addition, 
  "-":substraction, 
  "*":multiplication, 
  "/":division,
}

while stayloop:
  num_1 = int(input("What is the first number?"))
  operator = input("What is the operation? (+), (-), (*) or (/)")
  num_2 = int(input("What is the second number?"))
  calculation = operation[operator]
  answer = calculation(num_1, num_2)
  print(f"{num_1} {operator} {num_2} = {answer}")
  ask = input("Do you want to do another operation? yes (Y) or no (N)")
  if ask=='N':
    stayloop = False
