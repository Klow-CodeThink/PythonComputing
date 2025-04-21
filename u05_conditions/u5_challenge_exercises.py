###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Write a program to determine the ticket price based on age:
# Child (< 12): $10, 
# Adult (12-60): $20,
# Senior (> 60): $15.
# # Example:
# Input = 8.
# Output: "Ticket price is $10."
# # Ask the user to input the age

"""
age = int(input("Enter the age: "))
if age < 12:
    print("The ticket price is $10.")
elif age >= 12 and age <= 60:
    print("The ticket price is $20.")
else:
    print("The ticket price is $15.")
"""

#------------------------------------------------------------
# Exercise 2
# Write a program to calculate electricity bills based on units consumed.
# Rates:
# <= 100 units: $0.5/unit,
# <= 200 units: $0.75/unit,
# > 200 units: $1/unit. 
# Example:
# Input = 250
# Output: "Total bill is $212.5."
# Ask the user to input the units





#------------------------------------------------------------
# Exercise 3
# Write a program to check if a number is divisible by 2, 3, both, or neither.
# Example:
# Input = 6. 
# Output: "Divisible by both."
# Ask the user to input the number

"""
num = int(input("Enter the number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both.")
elif num % 2 == 0 and not (num % 3 == 0):
    print("Divisible by 2 only.")
elif num % 3 == 0 and not (num % 2 == 0):
    print("Divisible by 3 only.")
else:
    print("Not divisible by 2 or 3.")
"""

###########################################################