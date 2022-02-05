#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

a = len(letters)
b = len(numbers)
c = len(symbols)

password_list = []
for letter in range (0,nr_letters):
  k = random.randint(0, a-1)
  r = letters[k]
  password_list.append(r)

for symbol in range (0,nr_symbols):
  k = random.randint(0, c-1)
  r = symbols[k]
  password_list.append(r)

for letter in range (0,nr_numbers):
  k = random.randint(0, b-1)
  r = numbers[k]
  password_list.append(r)

random.shuffle(password_list)


password = ""
for key in password_list:
  password +=key
print(password)
   







