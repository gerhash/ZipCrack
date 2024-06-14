from cracker import Cracker,fileshandler
from ui import *
from colorama import Fore


def main():

    print(Fore.LIGHTYELLOW_EX + welcome)
    print(Fore.GREEN + string_sign)
    input(Fore.BLUE + "Press Enter to Continue >> ")

    print('\n\n\n')
    print(Fore.GREEN + zip_ui)
    filename = fileshandler('files','Select Zip File >> ')

    print('\n\n\n')
    print(Fore.MAGENTA + password_ui)
    passlist = fileshandler('wordlists','Select Passwords Txt File >>')

    zip = f'files/{filename}'
    passwords = f'wordlists/{passlist}'


    zipcracker = Cracker(zip,passwords)
    zipcracker.brute()



if __name__ == '__main__':
    main()