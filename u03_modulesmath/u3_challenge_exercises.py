###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Write a program to convert total minutes into hours and minutes.
# Your program must ask the user to input the number of minutes
# Example:
# Input = 185 minutes
# Output = 3 hours and 5 minutes.

"""
num1 = int(input("Enter the duration in minutes: "))
num2 = int(60)
floor_div = num1 // num2
modulus = num1 % num2
print(f"{floor_div} hours and {modulus} minutes")
# print("{} hours and {} minutes".format(floor_div, modulus))
"""

#------------------------------------------------------------
# Exercise 2
# Write a program to calculate how many notes of a specific
# denomination are needed to give change and how much remains.
# # Example:
# Change = $275
# Denomination = $50 
# Notes = 5
# Remaining = $25

"""
num1 = 275
num2 = 50
floor_div = num1 // num2
modulus = num1 % num2
print(f"You will receive {floor_div} ${num2}-notes for ${num1}, and ${modulus} change.")
# print("You will receive {} ${}-notes for ${}, and ${} change.".format(floor_div, num2, num1, modulus))
"""

#------------------------------------------------------------
# Exercise 3
# Write a program to calculate how many full containers are
# needed to ship items and how many are leftover.
# Use input for the number of items and the container capacity.
# Example:
# Items = 125
# Capacity = 30
# ->
# Full containers = 4
# Leftover = 5.

"""
items = 125
capacity = 30
full_containers = items // capacity
leftovers = items % capacity
print(f"{full_containers} full containers are needed to ship the items and there will be {leftovers} items remaining.")
"""

#------------------------------------------------------------
# Exercise 4
# Write a program to calculate the time it takes for an object
# to fall a certain height using the formula t = sqrt(2h/g).
# Example:
# Height = 20 m
# g = 9.8 m/s^2
# Output: 2.02 s.

"""
import math
h = 20
g = 9.8
t = math.sqrt(2*h/g)
print(f"It takes {t}s for the object to fall {h}m.")
"""

###########################################################
