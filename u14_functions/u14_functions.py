###################################################
# Part 1: Learning Exercises

# Exercise 1: A Simple Function
# Define a function that prints "Hello, World!" and call it.

def greet():
    print("Hello, World!")

# Call the function
greet()

#------------------------------------------------------------
# Exercise 2: Function with One Parameter
# Define a function that takes a name as a parameter and greets the user.

def greet_user(name):
    print(f"Hello, {name}!")

# Call the function with your name.
greet_user("Alice")

#------------------------------------------------------------
# Exercise 3: Function with Two Parameters
# Define a function that takes two numbers and prints their sum.

def add_numbers(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1 + num2}.")

# Call the function with two numbers.
add_numbers(5, 10)

#------------------------------------------------------------
# Exercise 4: Function with a Return Value
# Define a function that calculates the area of a rectangle.

def calculate_area(length, width):
    return length * width

# Call the function and store the result.
area = calculate_area(5, 3)
print(f"The area of the rectangle is {area} cm².")

#------------------------------------------------------------
# Exercise 5: Using Returned Values in Further Computations
# Define a function that calculates the perimeter of a rectangle.

def calculate_perimeter(length, width):
    return 2 * (length + width)


# Use both functions to calculate the area and perimeter.
length = 6
width = 4
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print(f"For a rectangle of length {length} cm and width {width} cm:")
print(f"Area: {area} cm², Perimeter: {perimeter} cm")

#------------------------------------------------------------
# Exercise 6: Demonstrating Local and Global Variables
# Define a function that modifies a local variable.

def local_variable_example():
    x = 10                                  # Local variable
    print(f"Inside the function, x is {x}")


# Outside the function.
x = 20                                      # Global variable
local_variable_example()
print(f"Outside the function, x is {x}")

###################################################

