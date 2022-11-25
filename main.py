from os import system, name
from password_gen import PasswordGenerator


def clear():
    system('cls' if name == 'nt' else 'clear')


def main():
    while True:
        pg = PasswordGenerator()
        clear()
        print("Welcome to the PyPassword Generator!")
        pg.get_nr_letters()
        pg.get_nr_upper_letters()
        pg.get_nr_symbols()
        pg.get_nr_numbers()
        while True:
            pg.generate_password()
            pg.print_password()
            if len(pg.password) > 0:
                save_password = input(
                    "\nDo you want to save this password? (y/n)\n").lower()
                if save_password == 'y':
                    pg.get_password_name()
                    pg.save_password()
            create_another = input(
                "\nDo you want to generate another password? (y/n)\n").lower()
            if create_another == 'y':
                same_settings = input(
                    "\nDo you want to use the same settings? (y/n)\n").lower()
                if same_settings == 'y':
                    clear()
                    pg.password_list = []
                    pg.password = ""
                    continue
                else:
                    main()
            else:
                input("\nPress enter to exit\n")
                clear()
                exit()


if __name__ == "__main__":
    main()
