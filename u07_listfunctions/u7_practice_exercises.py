###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 9: Summing Numbers in a List
# Write a program to calculate the sum of numbers in a list.

"""
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]


thesum = sum(list1)
print(thesum)

# or

thesum = 0
for i in list1:
    thesum = thesum + i
print(thesum)
"""

#------------------------------------------------------------
# Exercise 10: Finding the Maximum and Minimum
# Write a program to find the largest and smallest numbers in 
# a list using max() and min().

"""
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]


maxnum = max(list1)
print(f"The largest number is {maxnum}.")

minnum = min(list1)
print(f"The smallest number is {minnum}.")

# or

maxnum = list1[0]

for i in list1:
    if i > maxnum:
        maxnum = i

print(f"The largest number is {maxnum}.")


minnum = list1[0]

for i in list1:
    if i < minnum:
        minnum = i

print(f"The smallest number is {minnum}.")
"""

#------------------------------------------------------------
# Exercise 11: Iterating Through a List with Indices
# Write a program to print each element in a list with its index.

"""
fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)

# or

fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(fruits[i])
"""

#------------------------------------------------------------
# Exercise 12: Reversing a List
# Write a program to reverse the order of elements in a list.

"""
cities = ["New York", "London", "Paris", "Tokyo"]

cities.reverse()
print(cities)

or

cities2 = []
for c in cities:
    cities2.insert(0,c)
print(cities2)
"""

#------------------------------------------------------------
# Exercise 13: Sorting a List
# Write a program to sort a list of numbers in ascending order.

"""
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# in ascending order
list1 = sorted(list1)
print(list1)

# in descending order
list1 = sorted(list1, reverse = True)
print(list1)
"""

#------------------------------------------------------------
# Exercise 14: Removing Specific Index with del()
# Write a program to remove the third element in a list using del.
# Then print the updated list.

"""
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

del(list1[2])
print(list1)
"""

###########################################################