# A function returning multiple values
def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

# Calling the function and storing the returned values in a tuple
result = calculate(10, 5)

# Unpacking the returned tuple
add, sub, mul, div = result

print(f"Sum of 10 + 5 = {add}")   # Output: 15
print(f"Subtraction of 10 - 5 = {sub}")   # Output: 5
print(f"Multiplication of 10 x 5 = {mul}")   # Output: 50
print(f"Division of 10 / 5 = {div}")   # Output: 2.0
