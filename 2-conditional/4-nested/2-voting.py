# Check if a person is eligible to vote

age = int(input("What is your age? "))

if age >= 18:
    print("You are eligible to vote.")
    if age >= 65:
        print("You are also eligible for senior citizen benefits.")
    else:
        print("You are not eligible for senior citizen benefits.")
else:
    print("You are not eligible to vote.")
    if age < 5:
        print("You are too young to go to school.")
    else:
        print("You can go to school, but you are not eligible for a driving license yet.")
