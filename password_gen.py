import random
from password_strength import PasswordStats as ps


class PasswordGenerator:
    def __init__(self, password_name=None, nr_letters=None, nr_upper_letters=None, nr_symbols=None, nr_numbers=None, nr_chinese_chars=None) -> None:
        self.LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.UPPER_LETTERS = [letter.upper() for letter in self.LETTERS]
        self.NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '>', '<',
                        '^', '~', '@', '-', '_', 'ç', 'Ç', '`', '/', '|', 'ª', 'º', '¿',]
        self.CHINESE_CHAR = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '亿', '零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '貮', '參', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '两', '双', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '两',
                             '双', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '两', '双', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '两', '双', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '两', '双', '貳', '叄', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '佰', '仟', '萬', '億', '零', '两', '双']
        self.password_list = []
        self.password = ""
        self.password_name = password_name
        self.nr_letters = nr_letters
        self.nr_upper_letters = nr_upper_letters
        self.nr_symbols = nr_symbols
        self.nr_numbers = nr_numbers
        self.nr_chinese_chars = nr_chinese_chars

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

    def get_nr_chinese_char(self) -> None:
        while True:
            try:
                self.nr_chinese_char = int(
                    input("\nHow many chinese characters would you like?\n"))
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
        for char in range(1, self.nr_chinese_chars + 1):
            self.password_list += random.choice(self.CHINESE_CHAR)

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
