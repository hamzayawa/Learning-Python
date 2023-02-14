# The Mighty `if`, `if-else`, `nested-if-else` Statements in Python

![if-else](https://www.freecodecamp.org/news/content/images/2022/03/image-88.png)

The if, if-else statement is a powerful tool in Python that allows you to execute code blocks based on whether a certain condition is met. It works by first evaluating a condition and if the condition is true, executing the code in the if block. If the condition is false, it will execute the code in the else block.

Here is the basic syntax of an if-else statement in Python:

    if condition:
        # code to be executed if condition is true
    else:
        # code to be executed if condition is false

With the if-else statement, you can add an additional layer of logic to your code, making it more robust and easier to understand.

Here is an example of using the if-else statement to determine if a number is positive or negative:

    num = int(input("Enter a number: "))

    if num >= 0:
        print("The number is positive.")
    else:
        print("The number is negative.")

