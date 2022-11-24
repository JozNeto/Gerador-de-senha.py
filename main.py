from os import system, name
from password_gen import PasswordGenerator


def clear(): 
  system('cls' if name == 'nt' else 'clear')


def main():
  pg = PasswordGenerator()
  clear()
  print("Welcome to the PyPassword Generator!")
  pg.get_nr_letters()
  pg.get_nr_upper_letters()
  pg.get_nr_symbols()
  pg.get_nr_numbers()
  pg.generate_password()
  pg.print_password()
  save_password = input("\nDo you want to save this password? (y/n)\n")
  if save_password == 'y' or save_password == 'Y':
      pg.get_password_name()
      pg.save_password()
  create_another = input("\nDo you want to generate another password? (y/n)\n")
  if create_another == 'y' or create_another == 'Y':
      main()
  input("\nPress enter to exit\n")
  clear()


if __name__ == "__main__":
  main()