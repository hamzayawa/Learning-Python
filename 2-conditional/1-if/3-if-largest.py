# Check for the largest num
a = int(input("Enter a?: "))
b = int(input("Enter b?: "))
c = int(input("Enter c?: "))

if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")
