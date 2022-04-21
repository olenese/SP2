import bcrypt


def passwordhashing(password, passwordtest):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(salt)
    print(hashed)

    if bcrypt.checkpw(passwordtest.encode('utf-8'), hashed):
        print("It Matches")
    else:
        print("It Does not Match")

if __name__ == "__main__":
    passwordhashing("password", input("Enter Password: "))
