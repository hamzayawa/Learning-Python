# `Nested` `If-Else-Elif` Statements in Python


![Nested](/img/nested.jpeg)

In Python, you can use `nested` conditional statements to create more complex branching logic. This involves placing one conditional statement inside another. Here's an example:

    x = 10

    if x > 5:
        if x < 15:
            print("x is between 5 and 15")
        else:
            print("x is greater than 15")
    else:
        print("x is less than or equal to 5")

In this example, we have two `if` statements `nested` within one another. The first `if` statement checks whether `x` is greater than `5`. If that condition is true, the program moves on to the second if statement, which checks whether `x` is less than `15`. If both conditions are true, the program executes the code inside the `nested if` block, which prints the string `"x is between 5 and 15"`.

If the first `if` statement is true but the second `if` statement is false, the program moves on to the else block of the `nested if` statement, which executes the code inside the `else` block and prints the string `"x is greater than 15"`.

If the first `if` statement is false, the program moves on to the `else` block of the outer `if` statement, which executes the code inside the `else` block and prints the string `"x is less than or equal to 5"`.

You can use nested conditional statements to create more complex branching logic by adding more `if, else if (or elif), and else` statements inside the blocks of other conditional statements. Here's an example:

    x = 10

    if x > 5:
        if x < 15:
            print("x is between 5 and 15")
        elif x < 20:
            print("x is between 15 and 20")
        else:
            print("x is greater than or equal to 20")
    else:
        print("x is less than or equal to 5")

In this example, we've added an `elif` statement to the `nested if` block. If `x `is greater than `5` and less than `15`, the program executes the code inside the first `nested if` block and prints the string `"x is between 5 and 15"`. If `x` is not less than `15`, the program moves on to the `elif` statement, which checks whether `x` is less than `20`. If that condition is true, the program executes the code inside the `elif` block and prints the string `"x is between 15 and 20"`.


If both the `nested if and elif` conditions are false, the program moves on to the `else` block of the `nested if` statement, which executes the code inside the else block and prints the string "x is greater than or equal to 20".


If the first `if` statement is false, the program moves on to the else block of the outer `if` statement, which executes the code inside the `else` block and prints the string `"x is less than or equal to 5"`.

With these basic concepts in mind, you're ready to start using `nested` conditional statements in Python! And as you grow more experienced, you'll discover many more advanced features and techniques that make conditional statements an indispensable tool for writing high-quality, maintainable code.
