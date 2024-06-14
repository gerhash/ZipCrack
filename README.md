
<img src="https://github.com/gerhash/ZipCrack/assets/62940515/a9b2c900-540a-40f4-a4e5-cb471696e2b0" alt="zipcrack" width="700" height="600">

# Zip Crack - Zip Archive Password Bruteforce 
<img src="https://skillicons.dev/icons?i=py" alt="Skills" />

## Overview
Bruteforce tool to attack a Zip file

## Purpose
A zip file is a compressed archive that contains one or more files or directories. It's used to reduce the size of files for easier storage or transmission over the internet. When you unzip or extract a zip file, you restore the original files to their uncompressed state.
A password-protected zip file is one that has an added layer of security. When a zip file is protected by a password, you cannot unzip or extract its contents without entering the correct password first. This feature helps to safeguard the files within the zip archive from unauthorized access.

A bruteforce attack is a method used by attackers to crack passwords or encryption by systematically trying all possible combinations of characters until the correct one is found. 
In the context of password-protected zip files, a brute force attack would involve trying numerous combinations of passwords until the correct one is guessed, thereby gaining unauthorized access 
to the contents of the zip file. This type of attack can be time-consuming and resource-intensive but can potentially be effective if the password is not strong enough or if enough computing power is applied.

<img src="https://github.com/gerhash/ZipCrack/assets/62940515/82cdca90-b474-43cd-a5a4-d91e573b8a22" alt="bruteforce" width="460" height="250">

Your Python tool uses a zip file and a text file to perform a brute force attack. In the "/files" folder, you place the files you want to "crack," which are password-protected zip files. In the "/wordlist" folder,
you include text files containing a list of passwords, one per line. If the script successfully cracks the password, the extracted files are stored in the "/dumps" folder during execution.
<div>

</div>


## Usage
1. Install the required dependencies listed in `requirements.txt`.
   
 ```sh
   pip install -r requirements.txt
 ```

2. Run the main.py script to start.
   
 ```sh
  python main.py
 ```

3. Select the file you want to use Bruteforce

<img src="https://github.com/gerhash/ZipCrack/assets/62940515/d9495414-281a-469d-84f1-6e42f35e323f" alt="zip bruteforce" width="500" height="250">

4. Select the txt file who contains all the word combinations, you can find on internet, type wordlist.txt

<img src="https://github.com/gerhash/ZipCrack/assets/62940515/3f4ea7c3-b15d-4edd-b039-f0e61c1d7ef3" alt="wordlist bruteforce password cracking" width="500" height="210">

5. ZipCrack will try all the passwords contained in the chosen txt file in a few seconds, if it matches then the files will be dumped and you will know the password

<img src="https://github.com/gerhash/ZipCrack/assets/62940515/54ff5219-828e-423a-ac8d-f1b37b491b2d" alt="result password crack" width="380" height="600">




## Releases
#### v1.0
-  Zip Bruteforce


