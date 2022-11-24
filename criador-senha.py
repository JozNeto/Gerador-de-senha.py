import random
import os


def clear(): # clear the terminal
  os.system('cls' if os.name == 'nt' else 'clear')

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]

clear()
print("Welcome to the PyPassword Generator!")

def main():
  while True:
    nr_letters = None
    nr_symbols = None
    nr_numbers = None
    while True:
      try:
        if nr_letters == None and nr_symbols == None and nr_numbers == None:
          nr_letters = int(input("\nHow many letters would you like in your password?\n")) 
          nr_symbols = int(input("\nHow many symbols would you like?\n"))
          nr_numbers = int(input("\nHow many numbers would you like?\n"))
        elif nr_symbols == None and nr_numbers == None:
          nr_symbols = int(input("\nHow many symbols would you like?\n"))
          nr_numbers = int(input("\nHow many numbers would you like?\n"))
        elif nr_numbers == None:
          nr_numbers = int(input("\nHow many numbers would you like?\n"))
        break
      except ValueError:
        print("\nPlease, enter a number")
    
    password_list = []

    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(LETTERS))

    for char in range(1, nr_symbols + 1):
      password_list += random.choice(SYMBOLS)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(NUMBERS)

    random.shuffle(password_list) # randomize the list

    password = ""
    for char in password_list:
      password += char

    clear()
    print(f"Your password is: \n{password}\n")

    save_password = input("Do you want to save this password? (y/n)\n")

    if save_password == 'y' or save_password == 'Y':
      password_name = input("\nCreate a name for this password:\n")
      with open('my passwords.txt', 'a', encoding="utf-8") as file: # Create a file to save the passwords
        file.write(f"{password_name}\n{password}\n\n") # Save the password

    create_another = input("\nDo you want to generate another password? (y/n)\n")
    if create_another == 'y' or create_another == 'Y':
      clear()
      continue
    else:
      break
    

if __name__ == "__main__":
    main()

input("\nPress Enter to exit")
clear()
exit()