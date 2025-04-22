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


themax = max(list1)
print(themax)

themin = min(list1)
print(themin)

# or

maxnum = list1[0]

for i in list1:
    if i > maxnum:
        maxnum = i

print(maxnum)
"""

#------------------------------------------------------------
# Exercise 11: Iterating Through a List with Indices
# Write a program to print each element in a list with its index.

"""
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(fruits[i])
"""

# #------------------------------------------------------------
# # Exercise 12: Reversing a List
# # Write a program to reverse the order of elements in a list.

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

# #------------------------------------------------------------
# # Exercise 13: Sorting a List
# # Write a program to sort a list of numbers in ascending order.

"""
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

list1 = sorted(list1, reverse = True) # decending order / ascending (without reverse)
print(list1)
"""

# #------------------------------------------------------------
# # Exercise 14: Removing Specific Index with del()
# # Write a program to remove the third element in a list using del.
# # Then print the updated list.

"""
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

del(list1[2])
print(list1)
"""


# #------------------------------------------------------------

# What is my Chinese Zodiac sign?
# In not more than 10 lines of code, write a program 
# to calculate the Chinese Zodiac sign based on a 
# user's year of birth. (hint: it can be done in 5 lines)

# The most common method depends on Chinese New Year, 
# which is considered as the division of two animal years. 
# When a lunar year comes to an end, the animal will shift to next one. 
# Chinese people’s animal signs are marked by this method.

# How to Calculate Your Chinese zodiac sign mathematically?
# Divide your year of birth by 12 and get the remainder. 
# Each remainder corresponds to an animal sign below.

# 0: Monkey 1: Rooster 2: Dog 3: Pig 4: Rat 5: Ox 6: Tiger 
# 7: Rabbit 8: Dragon 9: Snake 10: Horse 11: Goat

# Sample Output
# Enter your birth year: 1977
# Your Chinese zodiac sign is: Snake


zodiac_animals = ['monkey','rooster','dog','pig','rat','ox',
                  'tiger''rabbit','dragon','snake','horse','goat']

birth_year = int(input("Enter your birth year: "))

remainder = birth_year % 12

zodiac_sign = zodiac_animals[remainder-1]

print(f"Your Chinese zodiac sign is: {zodiac_sign}")



# check that the user only inputs numbers
# and must be more than zero

while True:
    age = input("What is your age? ")

    # check if you input numbers
    if age.isdigit():
        age = int(age) 
     
        print(f"Your age is {age}")
        break
    else:
        print("You can only input numbers. ")



# Exercise 9: Counting Occurrences of a Value
# Write a program to count how many times a specific number 
# appears in a list.
# Example: Input = [1, 2, 2, 3], Check for 2.
numbers = [1, 2, 2, 3, 2, 4, 2, 5, 2]

count = 0
for n in numbers:
    if n == 2: # if number is 2
        count += 1 # change count by 1

print(count)



#------------------------------------------------------------
# Exercise 11: Ensuring All Numbers Are Positive
# Write a program to check that all numbers in a list are 
# positive. If any number is negative, remove it and print the 
# updated list.
numbers = [10, -5, 20, -15, 30, -25]
n2 = []

for n in numbers:
    if n >= 0:
        n2.append(n)

print(n2)