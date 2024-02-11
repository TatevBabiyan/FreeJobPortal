from RegisterValidation import *
from Login import LogIn
from getpass import getpass
import os
import hashlib

def menu():
    print("1. Registration")
    print("2. Login")
    print("3. Exit")


def main():
    choice = 0
    while choice != 3:
        menu()
        choice = int(input("Enter the Choice: "))
        if choice == 1:
            name = input("Enter your Name: ")
            surname = input("Enter your Surname: ")
            mail = input("Enter your E-Mail: ")
            password = getpass('Please enter your password (Your Password must contain: "!,@,#,$,%,^,&,*", Upperletter, Digit): ')
            reg = Validation(name, surname, mail, password)
            path = "database.txt"
            if reg:
                check_file = os.path.isfile(path)
                if not check_file:
                    with open("database.txt", "w") as f:
                        txt = f.read()
                        txt = txt.splitlines()
                        for i in txt:
                            if mail in i:
                                raise ValueError("Already an existing Mail")
                            else:
                                f.write(f"{reg.name},{reg.surname},{reg.email},{reg.password}\n")
                else:
                    with open("database.txt", "a") as f:
                        f.write(f"{reg.name},{reg.surname},{reg.email},{reg.password}\n")
                        print("Successful Registration")

        if choice == 2:
            email = input("Enter your E-Mail: ")
            password = getpass("Enter your Password: ")
            password_bytes = password.encode('utf-8')
            hash_object = hashlib.sha256(password_bytes)
            log = LogIn(email, hash_object.hexdigest())
            log.check_for_existence()

        if choice == 3:
            break


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(f"An error occurred: {e}")

        try_again = input("Do you want to try again? (y/n): ").lower()
        if try_again != 'y':
            break


