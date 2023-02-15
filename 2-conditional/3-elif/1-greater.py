# Check for greater than

x = 10
y = 20

if x > 10 and y > 20:
    print("x is greater than 10 and y is greater than 20")
elif x > 10 and y <= 20:
    print("x is greater than 10 and y is less than or equal to 20")
elif x <= 10 and y > 20:
    print("x is less than or equal to 10 and y is greater than 20")
else:
    print("x is less than or equal to 10 and y is less than or equal to 20")
