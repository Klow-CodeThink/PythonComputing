###########################################################
# Part 1: Learning Exercises 
# input() and and .format()

# Exercise 1: Using input() for Text
# Write a program to ask the user for their favorite color and display it.
# Example: If the user enters "blue", the program should display
# "Your favorite color is blue."

color = input("What is your favorite color? ")
print("Your favorite color is " + color + ".")

#------------------------------------------------------------
# Exercise 2: Understanding input() Behavior
# Write a program to ask the user for their age and display it.
# Example: If the user enters "15", display "Your age is 15."
# Note: Treat the input as a string for now.

age = input("Enter your age: ")
print("Your age is " + age + ".")

#------------------------------------------------------------
# Exercise 3: Comparing String Formatting Methods
# Write a program to ask the user for their name and age and display it
# in three different ways. Example: Input name = "John", age = 15

name = input("Enter your name: ")
age = input("Enter your age: ")

# Using + concatenation
print("Concatenation: " + name + " is " + age + " years old.")

# Using .format()
print("Using .format(): {} is {} years old.".format(name, age))

# Using f-strings
print(f"Using f-strings: {name} is {age} years old.")

#------------------------------------------------------------
# Exercise 4: Formatting a Message with .format()
# Write a program to display a sentence about favorite subjects.
# Example: Input subject = "Math", reason = "exciting"

subject = input("Enter your favorite subject: ")
reason = input("Why do you like it? ")
print("I like {} because it is {}.".format(subject, reason))

#------------------------------------------------------------
# Exercise 5: Comparing .format() and f-strings for a Calculation
# Write a program to calculate the sum of two numbers and format the
# output in two ways: using .format() and f-strings.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# num1 = int(num1)
# num2 = int(num2)
result = int(num1) + int(num2)

# Using .format()
print("Using .format(): The sum of {} and {} is {}.".format(num1, num2, result))

# Using f-strings
print(f"Using f-strings: The sum of {num1} and {num2} is {result}.")

###########################################################
