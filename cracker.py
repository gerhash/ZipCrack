import pyzipper
from datetime import datetime
import os
from ui import *  # Assuming this imports some UI related modules
from colorama import Fore, Back


class Cracker():
    def __init__(self, file, wordlist):
        self.file_path = file  # Initialize with the provided file path
        self.passwords = open(wordlist)  # Open the wordlist file for reading passwords

    def brute(self):
        for line in self.passwords.readlines():  # Iterate through each line in the wordlist
            passw = line.strip('\n')  # Remove newline characters from each password
            guess = self.extract(self.file_path, passw)  # Try to extract using each password
            if guess:  # If extraction is successful (password found), print and break
                print(Fore.GREEN + f"{found} \n \n\n Correct Password: " + Fore.CYAN + guess)
                break

    def extract(self, file, password):
        try:
            with pyzipper.AESZipFile(file, 'r') as zip_ref:  # Open the ZIP file with AES encryption
                dir = self.current_datetime()  # Generate a directory path based on current datetime
                zip_ref.extractall(path=dir, pwd=bytes(password, 'utf-8'))  # Extract files with the provided password
            return password  # Return the password if extraction is successful
        except pyzipper.BadZipFile:
            print(Fore.RED + f"{badzip_ui}")  # Handle case where ZIP file is corrupted or not a valid ZIP file
        except RuntimeError as e:
            print(Fore.RED + f"Not Valid: {password}")  # Handle runtime errors during extraction
        except Exception as e:
            print(Fore.RED + f"Error: {e}")  # Handle any other exceptions during extraction

    def current_datetime(self):
        now = datetime.now()  # Get the current datetime object
        datetime_string = now.strftime("%Y-%m-%d_%H-%M-%S")  # Format datetime as string
        return f'dumps/{datetime_string}'  # Return a path in 'dumps' directory with formatted datetime


def fileshandler(folder_path, text):
    while True:
        try:
            files = os.listdir(folder_path)  # List files in the specified folder path
            if not files:
                print(Fore.LIGHTYELLOW_EX + "Folder is Empty.")  # Inform if the folder is empty
                continue  # Continue the loop if the folder is empty

            print(Fore.LIGHTMAGENTA_EX + "Files: ")
            for i, file in enumerate(files, start=1):
                print(Back.CYAN + Fore.BLACK + f"{i}. {file}" + Back.RESET)  # Print each file in the folder

            filename = input(Back.RESET + Fore.BLUE + text)  # Prompt user to input filename

            file_path = os.path.join(folder_path, filename)  # Construct full path of selected file
            if os.path.exists(file_path):  # Check if the file exists in the specified folder
                print(Fore.YELLOW + f"File '{filename}' exists in '{folder_path}'.")
                return filename  # Return the selected filename if it exists
            else:
                print(Fore.RED + f"File '{filename}' does not exist in '{folder_path}'.")

        except FileNotFoundError:
            print(Fore.RED + f"'{folder_path}' does not exist.")  # Handle case where specified folder does not exist
            continue  # Continue the loop if folder does not exist
        except Exception as e:
            print(Fore.RED + f"Error: {e}")  # Handle any other exceptions during file handling
            continue  # Continue the loop in case of other exceptions
