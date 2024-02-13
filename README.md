# Job Portal Application

This is a simple application for a job portal that allows users to register, log in, and exit. 
The application stores user information in a text file called "database.txt". Here's how to use the application:

## Features:
- **Registration**: Users can register by providing their name, surname, email, and password. The password must contain special characters, uppercase letters, digits, and have a minimum length requirement.
- **Login**: Registered users can log in using their email and password. Passwords are securely stored using SHA256 encryption.
- **Error Handling**: The application handles exceptions gracefully and prompts the user to try again if an error occurs.
- **Exit**: Users can exit the application at any time.

## Usage:
1. Upon running the application, you will see a menu with options for registration, login, and exit.
2. Choose option 1 to register by providing your name, surname, email, and password.
3. Choose option 2 to log in using your registered email and password.
4. After successful login, you will be presented with a menu to perform various actions (e.g., set name, set surname, set password).
5. Choose option 3 to exit the application.

## Dependencies:
- Python 3.x
- getpass: A Python library for getting passwords from the user without displaying them on the screen.
- hashlib: A Python library for secure hash and message digest algorithms.

## Files:
- **main.py**: Contains the main functionality for user interaction.
- **RegisterValidation.py**: Module for validating user registration data.
- **Login.py**: Module for user login functionality.

## Descriptors:
- NameValidationDescriptor: Validates the format of a user's name.
- SurnameValidationDescriptor: Validates the format of a user's surname.
- EmailValidatonDescriptor: Validates the format of a user's email address.
- PasswordValidationDescriptor: Validates the format of a user's password.
