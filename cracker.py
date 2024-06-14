import pyzipper
from datetime import datetime
import os
from ui import *
from colorama import Fore,Back

class Cracker():
    def __init__(self, file, wordlist):
        self.file_path = file
        self.passwords = open(wordlist)

    def brute(self):
        for line in self.passwords.readlines():
            passw = line.strip('\n')
            guess = self.extract(self.file_path, passw)
            if guess:
                print(Fore.GREEN + f"{found} \n \n\n Correct Password: " + Fore.CYAN + guess)
                break
    def extract(self,file, password):
        try:
            with pyzipper.AESZipFile(file, 'r') as zip_ref:
                dir = self.current_datetime()
                zip_ref.extractall(path=dir,pwd=bytes(password, 'utf-8'))
            return password
        except pyzipper.BadZipFile:
            print(Fore.RED + f"{badzip_ui}")
        except RuntimeError as e:
            print(Fore.RED + f"Not Valid: {password}")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

    def current_datetime(self):
        # Ottieni l'oggetto datetime corrente
        now = datetime.now()
        # Formatta la data e l'ora come stringa
        datetime_string = now.strftime("%Y-%m-%d_%H-%M-%S")
        return f'dumps/{datetime_string}'


def fileshandler(folder_path, text):
    while True:
        try:
            files = os.listdir(folder_path)
            if not files:
                print(Fore.LIGHTYELLOW_EX + "Folder is Empty.")
                continue  # Continua il ciclo se la cartella è vuota

            print(Fore.LIGHTMAGENTA_EX + "Files: ")
            for i, file in enumerate(files, start=1):
                print(Back.CYAN + Fore.BLACK + f"{i}. {file}" + Back.RESET)

            filename = input(Back.RESET + Fore.BLUE + text)

            # Verifica se il file ZIP esiste nella cartella specificata
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path):
                print(Fore.YELLOW + f"File '{filename}' exists in '{folder_path}'.")
                return filename
            else:
                print(Fore.RED + f"File '{filename}' does not exist in '{folder_path}'.")

        except FileNotFoundError:
            print(Fore.RED + f"'{folder_path}' does not exist.")
            continue  # Continua il ciclo se la cartella non esiste
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            continue  # Continua il ciclo in caso di altre eccezioni
