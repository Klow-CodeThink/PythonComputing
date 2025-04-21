###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 7: Simulating Two Dice Rolls
# Write a program to simulate the roll of a 6-sided die two times
# and display the results. Example: Output = 4, 6.

"""
import random
rannum1 = random.randint(1,6)
rannum2 = random.randint(1,6)
print(f"Output = {rannum1}, {rannum2}")
"""

#------------------------------------------------------------
# Exercise 8: Floor Division for Groups
# Write a program to calculate how many full groups can be formed 
# and how many items are leftover. Example: 25 students divided 
# into groups of 4 = 6 groups and 1 leftover.

"""
tt_stu = int(input("Enter the total number of students: "))
gps_of = int(input("Enter the number of students in each group: "))
floor_div = tt_stu // gps_of
mod = tt_stu % gps_of
print(f"{tt_stu} students divided into groups of {gps_of} = {floor_div} groups and {mod} leftover.")
"""

#------------------------------------------------------------
# Exercise 9: Rounding for Fuel Costs
# Write a program to calculate the total cost of fuel rounded up 
# to the nearest dollar. Example: If the fuel cost is 47.89, the 
# total is 48.

"""
import math
cost = 47.89
rounded = math.ceil(cost)
print(f"If the fuel cost is ${cost}, the total is ${rounded}.")
"""

#------------------------------------------------------------
# Exercise 10: Floor Division for Age Conversion
# Write a program to calculate someone's age in decades and 
# remaining years. Example: Age = 29 -> Decades = 2, Years = 9.

"""
age = int(input("Enter the age: "))
floor_div = age // 10
mod = age % 10
print(f"Age = {age} -> Decade = {floor_div}, Years = {mod}")
"""

#------------------------------------------------------------
# Exercise 11: Calculating Items in Boxes
# Write a program to calculate how many full boxes are needed to 
# pack items and how many items are leftover. Example: If there 
# are 53 items and each box holds 12, the output is:
# Full boxes = 4, Leftover = 5.

"""
tt_items = int(input("What is the total number of items? "))
items_each = int(input("How many items can each box hold? "))
floor_div = tt_items // items_each
mod = tt_items % items_each
print(f"Full boxes = {floor_div}, Leftover = {mod}")
"""

###########################################################

