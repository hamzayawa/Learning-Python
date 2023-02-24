# Simple Password validation program
print("<===Simple Password validation===>")
print()

password = input("Enter a password: ")
while len(password) < 8 or password.islower():
    print("Password must be at least 8 characters and contain at least one uppercase letter.")
    password = input("Enter a password: ")
