###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.

# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])

"""
def greet(arg_users):
    for users in arg_users:
        print(f"Hello, {users}!")

user_list = ["Alice", "Bob", "Charlie"]
greet(user_list)
"""

#------------------------------------------------------------
# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.

# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

"""
# test
def add_num(a, b):              # defines a function called add_num that takes two parameters a and b
    sum = a + b                 # inside the function, add a and b, and store the result in variable called sum
    return sum                  # function sends back (returns) the calculated sume to wherever the function is called

thesum = add_num(3, 5)          # calls the function with 3 and 5, and store the returned value in thesum
print(f"The sum is: {thesum}")  # prints result


# actual
def cal_num(a, b, op):          # defines a function with two numbers and one operator as input
    if op == "+":               # checks each operation: add, subtract, multiply, divide
        result = a + b
        return result
    elif op == "-":
        result = a - b
        return result
    
    elif op == "x":
        result = a * b
        return result
    
    elif op == "/":
        result = a / b
        return result
    
    else:                       # if the operation is not recognised, return "Invalid operation"
        return "Invalid operation"

calculator = cal_num(10, 2, "=")        # calls the function
print(f"The result is: {calculator}")   # prints result
"""

#------------------------------------------------------------
# Exercise 9: Palindrome Checker
# Write a function that checks if a string is a palindrome.

# Test the function with different words.
# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))

"""
# original
def pal(word):                              # defines a function that takes a string input word
    if word == word[::-1]:                  # reverses the string using slicing, checks if word is same when reversed
        return "True"                       # returns result as string
    else:
        return "False"

pal_result = pal("radar")                       # calls the function with word "radar"
print(f"Is 'radar' a palindrome? {pal_result}")   # prints result


# improved
def pal(word):
    word = word.lower()                         # converts input to all lowercase (case insensitive checking)
    return word == word[::-1]                   # reverses word, compares original and reversed word, returns True/False (Real Booleans)

pal_result = pal("hello")
print(f"Is 'hello' a palindrome? {pal_result}")
"""

#------------------------------------------------------------
# Exercise 10: Display Multiplication Table
# Write a function that takes a number and prints its multiplication table.

# Call the function with a number.
# multiplication_table(5)

"""
def mul_tables(mul):                        # defines a function named mul_tables that takes one input (mul)
    for i in range(1, 11):                  # a loop that counts from 1 to 10
        print(f"{mul} x {i} = {mul * i}")   # for each number i, it prints the multiplication result

mul_tables(5)                               # call the function and pass (5) as the number to build the 5 timestable
"""

###########################################################
