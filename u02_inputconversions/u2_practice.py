# U2 - Exercise 1
# Write a program to ask the user for their first and last name.
# Use .format() to display a full greeting message.
# Example:
# Input: first_name = "John", last_name = "Doe"
# Output: "Hello, John Doe! Welcome to Python programming."
# You must follow the exact sentence format above to complete this exercise.

"""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, {} {}! Welcome to Python programming.".format(first_name, last_name))
"""

# U2 - Exercise 2
# Write a program to ask the user for the length and width of a rectangle,
# calculate its perimeter and area, and display the results using .format().
# Example: Input length = 5, width = 3
# Output: "Perimeter: 16, Area: 15."
# You must use the .format() and output exactly as above to complete this exercise.

"""
length = 5
breadth = 3
perimeter = 2 * (length + breadth)
area = length * breadth
print("Perimeter: {}, Area: {}".format(perimeter, area))
"""

# U2 - Exercise 3
# Write a program to ask the user for a temperature in Celsius, convert it
# to Fahrenheit, and display the result using .format().
# Use the formula: Fahrenheit = (Celsius * 9/5) + 32.
# Example:
# Input: Celsius = 25
# Output: "25°C is equal to 77°F."


cel = int(input("Enter the temperature: "))
fah = int((cel * 9/5) + 32)
print("{}°C is equal to {}°F.".format(cel, fah))

