###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 8: Finding the Smallest Without Built-In Functions
# Write a program to find the smallest number in a list without 
# using min().

"""
list1 = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

minnum = list1[0]

for i in list1:
    if i < minnum:
        minnum = i

print(f"The smallest number is {minnum}.")
"""

#------------------------------------------------------------
# Exercise 9: Counting Occurrences of a Value
# Write a program to count how many times a specific number 
# appears in a list.
# Example: Input = [1, 2, 2, 3], Check for 2.

"""
list1 = [1, 2, 2, 3, 2, 4, 2, 5, 2]

count = 0

for i in list1:
    if i == 2:
        count = count + 1

print(count)
"""

#------------------------------------------------------------
# Exercise 10: Removing Duplicates from a List
# Write a program to remove duplicate values from a list.
# Example: Input = [1, 2, 2, 3, 4, 4], Output = [1, 2, 3, 4].





#------------------------------------------------------------
# Exercise 11: Ensuring All Numbers Are Positive
# Write a program to check that all numbers in a list are 
# positive. If any number is negative, remove it and print the 
# updated list.

"""
list1 = [10, -5, 20, -15, 30, -25]

list2 = []

for i in list1:
    if i >= 0:
        list2.append(i)

print(list2)
"""

###########################################################