import random


class PasswordGenerator:
    def __init__(self) -> None:
        self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.UPPER_LETTERS = [letter.upper() for letter in self.LETTERS]
        self.NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<', '^', '~', '@', '-', '_', 'ç', 'Ç','`', '/', '|', 'ª', 'º', '¿',]
        self.password_list = []
        self.password = ""
        self.password_name = ""
        self.nr_letters = None
        self.nr_upper_letters = None
        self.nr_symbols = None
        self.nr_numbers = None


    def get_nr_letters(self) -> None:
        while True:
            try:
                if self.nr_letters == None:
                    self.nr_letters = int(input("\nHow many letters would you like in your password?\n")) 
                break
            except ValueError:
                print("\nPlease, enter a number")


    def get_nr_upper_letters(self) -> None:
        while True:
            try:
                if self.nr_upper_letters == None:
                    self.nr_upper_letters = int(input("\nHow many upper letters would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")


    def get_nr_symbols(self) -> None:
        while True:
            try:
                if self.nr_symbols == None:
                    self.nr_symbols = int(input("\nHow many symbols would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")


    def get_nr_numbers(self) -> None:
        while True:
            try:
                if self.nr_numbers == None:
                    self.nr_numbers = int(input("\nHow many numbers would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")


    def generate_password(self) -> None:
        for char in range(1, self.nr_letters + 1):
            self.password_list.append(random.choice(self.LETTERS))
        for char in range(1, self.nr_upper_letters + 1):
            self.password_list += (random.choice(self.UPPER_LETTERS))
        for char in range(1, self.nr_symbols + 1):
            self.password_list += random.choice(self.SYMBOLS)
        for char in range(1, self.nr_numbers + 1):
            self.password_list += random.choice(self.NUMBERS)

        random.shuffle(self.password_list)
        for char in self.password_list:
            self.password += char


    def print_password(self) -> None:
        print(f"\nYour password is: \n{self.password}")


    def get_password_name(self) -> None:
        self.password_name = input("\nName this password\n")


    def save_password(self) -> None:
        with open("my passwords.txt", "a", encoding="utf-8") as file:
            file.write(f"{self.password_name}\n{self.password}\n\n")

