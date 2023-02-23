# Print Fibonacci numbers using for loop
n = 20 # set the number of Fibonacci numbers to print
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
