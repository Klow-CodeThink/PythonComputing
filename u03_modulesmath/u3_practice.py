# U3 - Exercise 1
# Write a program to convert total minutes into hours and minutes.
# Your program must ask the user to input the number of minutes
# Example:
# Input = 185 minutes
# Output = 3 hours and 5 minutes.


num1 = int(input("Enter the duration in minutes: "))
num2 = int(60)
floor_div = num1 // num2
modulus = num1 % num2
# print("{} hours and {} minutes".format(floor_div,modulus))








# U3 - Exercise 2
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
# print("You will receive {} ${}-notes for ${}, and ${} change.".format(floor_div,num2,num1,modulus))
print(f"You will receive {floor_div} ${num2}-notes for ${num1}, and ${modulus} change.")
"""

