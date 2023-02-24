# Advance Password Validation

import re

password = input("Enter a password: ")

while True:
    if len(password) < 8:
        print("Password must be at least 8 characters long")
    elif not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter")
    elif not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter")
    elif not re.search(r'[0-9]', password):
        print("Password must contain at least one number")
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("Password must contain at least one special character")
    else:
        print("Password is valid")
        break

    password = input("Enter a new password: ")

