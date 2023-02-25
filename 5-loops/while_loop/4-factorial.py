# Example: Computing the factorial of a number using a while loop

number = int(input("Enter a positive integer: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print("The factorial of the given number is:", factorial)
