import random
import string
import os
import sys

characters = list(string.ascii_letters + string.digits + "!@$%&#/\?*()")
special_characters = list("!@$%&#/\?*()")
special_characters_with_whitespace = list("!@$%&#/\?*() ")

def randomcharacter(length):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    result = [ ]
    for x in password:
        case = random.randint(0,1)
        if case == 0:
            result += x.upper()
        else:
            result += x.lower()
    return "".join(result)


def passphraseNO(length):
    passphrase = []
    while len(passphrase) != length:    
        with open("wordlistNOB.txt", "r") as file:
            for line in file:
                passphrase.append(line.strip("\n"))
                








def passphrase_generator():
    passphrase = []

    phrase_length = int(input("Please enter the amount of words in the passtext: "))

    random.shuffle(special_characters_with_whitespace)

    all_passwords = []
    if input("Do you want a Norwegian passphrase? (y/n): ") == "y":    
        with open("wordlistNOB.txt", "r") as file:
            for line in file:
                all_passwords.append(line.strip("\n"))
    else:
        with open("wordlistEN.txt", "r") as file:
            for line in file:
                all_passwords.append(line.strip("\n"))
        

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

