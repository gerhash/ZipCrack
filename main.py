import pyzipper





def extract(file,password):
    try:
        with pyzipper.AESZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(pwd=bytes(password,'utf-8'))
        return password
    except pyzipper.BadZipFile:
        print("Error: ZIP not valid")
    except RuntimeError as e:
        print(f"Not Valid: {password}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    zip_file_path = 'secretpic.zip'
    passwords = open('passwords.txt')
    for line in passwords.readlines():
        passw = line.strip('\n')
        guess = extract(zip_file_path,passw)
        if guess:
            print(f"Success: {guess}")
            break



if __name__ == '__main__':
    main()