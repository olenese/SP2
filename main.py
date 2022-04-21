import bcrypt
import mysql.connector
class CheckPasswords:

    def passwordhashing(password, passwordtest):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        print(salt)
        print(hashed)

        if bcrypt.checkpw(passwordtest.encode('utf-8'), hashed):
            print("It Matches")
        else:
            print("It Does not Match")

    def dbconnect(username_input, password_input):
        mydb = mysql.connector.connect(
            host="172.105.131.62",
            user="olenese",
            passwd=input("Enter your password: "),
            database="userlogins"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT hash FROM logins WHERE username = '" + username_input + "'")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        mydb.close()

    def authcheck():
        for username in user_database:
            if username_input == username:
                password_input_hash = hashlib.md5(password_input.encode()).hexdigest()
                password_hash = user_database[username]
                return password_hash == password_input_hash
        return False


if __name__ == "__main__":
    CheckPasswords.passwordhashing("nice try", "nice try")
    CheckPasswords.dbconnect()


