rows = int(input("Enter the number of rows: "))

k = 2 * rows - 2  # print space
for i in range(-1, rows):
    # Inner loop will print the number of space.
    for j in range(0, k):
        print(end=" ")
    k = k - 1  # decrement k value for each iteration
    # This inner loop will print the number o stars
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")
