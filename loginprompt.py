import hashlib
import os
import getpass


# Goal = login prompt
# user_database
# Ask for username and password
# Function to check username
# Function to check passwords
# Hash the passwords

# administrator = password123
# sysadmin = mypassword
# basic_user = random_password


user_database = {
    "administrator": "482c811da5d5b4bc6d497ffa98491e38",
    "sysadmin": "34819d7beeabb9260a5c854bc85b3e44",
    "basic_user": "3d7cb72b7a5a03870b9d79d050ed61c4"
}
username_input = None
password_input = None


# def clear only works in terminal
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def auth_check():
    for username in user_database:
        if username_input == username:
            password_input_hash = hashlib.md5(password_input.encode()).hexdigest()
            password_hash = user_database[username]
            return password_hash == password_input_hash
    return False


continue_prompt = True
while continue_prompt:
    username_input = input("What is your username? ")
    password_input = input("What is your password? ") # <----- Only for dev.
    # password_input = getpass.getpass("What is your password? ")     <----  Only runs in Terminal
    if auth_check():
        print("Username and password is correct!")
        break
    else:
        print("Username or password is incorrect!")
        continue_prompt = input("Try again? (Y/N) ").lower() == "y"
        if continue_prompt:
            clear()