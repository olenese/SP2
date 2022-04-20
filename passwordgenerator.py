import random
import string
import os
import sys

characters = list(string.ascii_letters + string.digits + "!@$%&#/\?^*()")
special_characters = list("!@$%&#")

def passwordgenerator():
    word_length = int(input("Enter password lenght: "))
    if word_length <= 8:
        print("Not secure password, the minimum wordlength should be 8 characters!!!")
        word_length = int(input("Enter password lenght: "))

    random.shuffle(characters)

    password = []
    for i in range(word_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

    ready_password = "".join(password)

    with open("Passwords.txt", "a") as f:
        location = input("Where are you using this password?: ")
        # print(location," : ", ready_password,  file=f)
        f.write(location + " : " + ready_password)
    
    print("Password has been vaulted!")

def passphrase_generator():
    passphrase = []

    phrase_length = int(input("Please enter the amount of words in the passtext: "))

    random.shuffle(special_characters)

    all_passwords = []
    with open("rockyou.txt", "r") as file:
        for line in file:
            all_passwords.append(line.strip("\n"))
        # all_passwords = file.readlines()
    
#    for i in range(5):
#        print(all_passwords[i])

#    for i in range(phrase_length):
#        with open("rockyou.txt", "r") as file:
#            allText = file.read()
#            words = list(map(str, allText.split()))
#        passphrase.append(random.choice(words))

    for i in range(phrase_length):
        passphrase.append(random.choice(all_passwords))
        
    print(passphrase)


    ready_passphrase = ""
    for x in passphrase:
        ready_passphrase += random.choice(special_characters) + x
    
    print(ready_passphrase)

    with open("Passwords.txt", "a") as f:
        location = input("Where are you using this password?: ")
        #print(location," : ", ready_passphrase, file=f)
        f.write(location + " : " + ready_passphrase)
    print("Password has been vaulted!")


if __name__ == "__main__":
    choice = int(input("What type of password would you like? \n Type 1 for Password \n Type 2 for Passphrase: \n"))
    if choice == 1:
        passwordgenerator()
    elif choice == 2:
        passphrase_generator()
