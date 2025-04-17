
#####################################################

# Part 1: Learning Exercises

# Exercise 1: Importing Modules
# Write a program to use the math module for calculations.
# Example: Calculate the square root of 16 and the power of 2^3.
import math  # Importing the math module
sqrt_value = math.sqrt(16)
power_value = math.pow(2, 3)
print("Square root of 16 is:", sqrt_value)
print("2 to the power of 3 is:", power_value)


#------------------------------------------------------------
# Exercise 2: Modulus and Floor Division
# Write a program to calculate the modulus and floor division
# of two numbers. Example: 17 divided by 5.
num1 = 17
num2 = 5
modulus = num1 % num2
floor_div = num1 // num2
print("17 % 5 is:", modulus)
print("17 // 5 is:", floor_div)


#------------------------------------------------------------
# Exercise 3: Using Rounding Methods
# Write a program to round a number using round(), math.ceil(),
# and math.floor(). Example: number = 5.67.
number = 5.67
rounded = round(number)
ceiled = math.ceil(number)
floored = math.floor(number)
print("Rounded:", rounded, "Ceiled:", ceiled, "Floored:", floored)


#------------------------------------------------------------
# Exercise 4: Floor Division for Time Conversion
# Write a program to convert total seconds into minutes and 
# seconds using floor division and modulus. Example: 125 seconds
# = 2 minutes and 5 seconds.
total_seconds = 125
minutes = total_seconds // 60
seconds = total_seconds % 60
print("Minutes:", minutes, "Seconds:", seconds)


#------------------------------------------------------------
# Exercise 5: Rounding for Pricing
# Write a program to calculate the total price of an item after 
# rounding up to the nearest dollar. Example: If the price is 
# 19.75, the total is 20.
price = 19.75
rounded_price = math.ceil(price)
print("Rounded total price is:", rounded_price)


#------------------------------------------------------------
# Exercise 6: Generating Random Integers
# Write a program to generate a random number between 1 and 10.
# Example: The output could be any number from 1 to 10.
import random
random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)


#####################################################