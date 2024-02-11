import os
import getpass
from NameValidationDescriptor import NameValidation
from SurnameValidationDescriptor import SurnameValidation
from EmailValidationDescriptor import EmailValidation
from PasswordValidationDescriptor import PasswordValidation

class LogIn:
    new_name = NameValidation()
    new_surname = SurnameValidation()
    new_mail = EmailValidation()
    new_password = PasswordValidation()

    def __init__(self, mail, password):
        self._mail = mail
        self._password = password

    def check_for_existence(self):
        path = "database.txt"
        if os.path.isfile(path):
            with open("database.txt", "r") as f:
                txt = f.readlines()
                for line in txt:
                    if self._mail in line and self._password in line:
                        print("Successful Login")
                        self.menu()
        else:
            raise FileExistsError("Not Found")


    def menu(self):
        path = "database.txt"
        update_line = []
        print("1. Set Name, 2. Set Surname, 3. Set E-Mail, 4. Set Password, 5. Back to Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter New Name: ")
            with open(path, "r") as f:
                for line in f:
                    parts = line.split(",")
                    if self._mail in parts:
                        self.new_name = name
                        parts[0] = self.new_name
                    update_line.append(",".join(parts))
            with open(path, "w") as f:
                f.writelines(update_line)
                print("Successful Changing")
        elif choice == 2:
            surname = input("Enter New Surname: ")
            with open(path, "r") as f:
                for line in f:
                    parts = line.split(",")
                    if self._mail in parts:
                        self.new_surname = surname
                        parts[1] = self.new_surname
                    update_line.append(",".join(parts))
            with open(path, "w") as f:
                f.writelines(update_line)
                print("Successful Changing")
        elif choice == 3:
            mail = input("Enter New E-Mail: ")
            with open(path, "r") as f:
                for line in f:
                    parts = line.split(",")
                    if self._mail in parts:
                        self.new_mail = mail
                        parts[2] = self.new_mail
                    update_line.append(",".join(parts))
            with open(path, "w") as f:
                f.writelines(update_line)
                print("Successful Changing")
        elif choice == 4:
            password = getpass.getpass("Enter New Password: ")
            with open(path, "r") as f:
                for line in f:
                    parts = line.split(",")
                    if self._password in parts[-1][:-1]:
                        self.new_password = password
                        parts[3] = self.new_password
                    update_line.append(",".join(parts))
            with open(path, "w") as f:
                f.writelines(update_line)
                print("Successful Changing")
        elif choice == 5:
            return False
        else:
            print("Invalid choice")
