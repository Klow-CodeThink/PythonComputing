###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 6: Greeting with .format()
# Write a program to ask the user for their name and print a greeting
# using .format(). Example:
# Input: name = "Alice"
# Output: "Hello, Alice! Have a great day!"

"""
name = "Alice"
print("Hello, {}! Have a great day!".format(name))
"""

#------------------------------------------------------------
# Exercise 7: Adding Two Numbers with .format()
# Write a program to ask the user for two numbers, convert them to integers,
# add them, and display the result using .format(). Example:
# Input: 5, 3
# Output: "The sum of 5 and 3 is 8."

"""
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum of {num1} and {num2} is {num1 + num2}.")
"""

#------------------------------------------------------------
# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."

"""
import math
radius = input("Enter the radius of the circle: ")
radius = float(radius)
area = 3.14 * radius ** 2
print("The area of the circle is {}.".format(area))
"""

#------------------------------------------------------------
# Exercise 9: Describing a Favorite Activity
# Write a program that asks the user for their favorite hobby and explains
# why they like it. Format the output using .format().
# Example: hobby = "reading", reason = "relaxing"

"""
hobby = input("What is your hobby? ")
reason = input("Why do you enjoy it? ")
print("I enjoy {} because it is {}.".format(hobby, reason))
"""

###########################################################