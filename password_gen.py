import random
from password_strength import PasswordStats as ps


class PasswordGenerator:
    def __init__(self, password_name=None, nr_letters=None, nr_upper_letters=None, nr_symbols=None, nr_numbers=None) -> None:
        self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.UPPER_LETTERS = [letter.upper() for letter in self.LETTERS]
        self.NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<',
                        '^', '~', '@', '-', '_', 'ç', 'Ç', '`', '/', '|', 'ª', 'º', '¿',]
        self.password_list = []
        self.password = ""
        self.password_name = password_name
        self.nr_letters = nr_letters
        self.nr_upper_letters = nr_upper_letters
        self.nr_symbols = nr_symbols
        self.nr_numbers = nr_numbers

    def get_nr_letters(self) -> None:
        while True:
            try:
                self.nr_letters = int(
                    input("\nHow many letters would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")

    def get_nr_upper_letters(self) -> None:
        while True:
            try:
                self.nr_upper_letters = int(
                    input("\nHow many upper letters would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")

    def get_nr_symbols(self) -> None:
        while True:
            try:
                self.nr_symbols = int(
                    input("\nHow many symbols would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")

    def get_nr_numbers(self) -> None:
        while True:
            try:
                self.nr_numbers = int(
                    input("\nHow many numbers would you like?\n"))
                break
            except ValueError:
                print("\nPlease, enter a number")

    def generate_password(self) -> None:
        for char in range(1, self.nr_letters + 1):
            self.password_list += random.choice(self.LETTERS)
        for char in range(1, self.nr_upper_letters + 1):
            self.password_list += random.choice(self.UPPER_LETTERS)
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

    def get_password_strength(self) -> str:
        if len(self.password) != 0:
            password_strength = ps(self.password)
            if password_strength.strength() <= 0.3:
                self.password_stength = "Very weak"
            elif password_strength.strength() >= 0.3 and password_strength.strength() <= 0.5:
                self.password_stength = "Weak"
            elif password_strength.strength() >= 0.5 and password_strength.strength() <= 0.6:
                self.password_stength = "Medium"
            elif password_strength.strength() >= 0.6 and password_strength.strength() <= 0.8:
                self.password_stength = "Strong"
            elif password_strength.strength() >= 0.8:
                self.password_stength = "Very strong"
            return self.password_stength
        else:
            return "No password generated"
