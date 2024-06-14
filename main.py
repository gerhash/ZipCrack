from cracker import Cracker, fileshandler
from ui import *  # Importing UI related strings and variables
from colorama import Fore  # Importing colorama's Fore for colored output

def main():
    # Display welcome message and sign using colorama's Fore
    print(Fore.LIGHTYELLOW_EX + welcome)
    print(Fore.GREEN + string_sign)
    print('\n\n')
    input(Fore.BLUE + "Press Enter to Continue >> ")  # Prompt user to press Enter to continue

    print('\n\n\n')
    print(Fore.GREEN + zip_ui)  # Display message for selecting ZIP file
    filename = fileshandler('files', 'Select Zip File >> ')  # Call fileshandler to select ZIP file

    print('\n\n\n')
    print(Fore.MAGENTA + password_ui)  # Display message for selecting passwords file
    passlist = fileshandler('wordlists', 'Select Passwords Txt File >> ')  # Call fileshandler to select passwords file

    # Construct paths to the selected files
    zip_file = f'files/{filename}'
    passwords_file = f'wordlists/{passlist}'

    # Create an instance of Cracker with the selected files and crack the ZIP file
    zipcracker = Cracker(zip_file, passwords_file)
    zipcracker.brute()

if __name__ == '__main__':
    main()
