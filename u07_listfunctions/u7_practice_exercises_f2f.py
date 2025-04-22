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

# #------------------------------------------------------------

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

# #------------------------------------------------------------

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