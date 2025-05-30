###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 7: Multiplication Table with While Loop
# Write a program to print the multiplication table of 7 up to 10.
# Example: 7 x 1 = 7, ..., 7 x 10 = 70.

"""
i = 1
num = 7
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i = i + 1
"""

#------------------------------------------------------------
# Exercise 8: Sum of Even Numbers
# Write a program to calculate the sum of even numbers between 1 
# and 20 using a while loop. Example: Output = 110.

"""
i = 2
sum = 0
while i <= 20:
    sum = sum + i
    i = i + 2

print(f"The sum is {sum}.")
"""

#------------------------------------------------------------
# Exercise 9: Guessing Game
# Write a program where the user has to guess a random number 
# between 1 and 10. Keep prompting until they guess correctly.

"""
import random
rannum = random.randint(1,10)
print(rannum)


while True:

    guess = int(input("Guess my number: "))

    if guess == rannum:
        print("You are correct!")
        break
    else:
        print("Try again.")
"""

#------------------------------------------------------------
# Exercise 10: Input Validation for a Password
# Write a program that keeps asking the user to enter a password.
# If the password is correct, print "Access granted."

"""
while True:
    password = input("Enter the password: ")

    if password == "learn2code":
        print("Access granted.")
        break
    else:
        print("Access denied.")
"""

#------------------------------------------------------------
# Exercise 11: Printing Fibonacci Sequence
# Write a program to print the first 10 numbers in the Fibonacci
# sequence using a while loop. The Fibonacci sequence is a series 
# of numbers where each number is the sum of the two preceding 
# ones. It starts with 0 and 1.
# Example: Output = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.





#------------------------------------------------------------
# Exercise 12: Custom Pattern
# Write a program to print the following pattern:
# *
# **
# ***
# ****
# *****

"""
i = 1               # Initialize counter
while i <= 5:       # Loop until i is greater than 5
    print("*" * i)  # Print i number of asterisks
    i += 1          # Increment i by 1 or i = i + 1
"""

"""
for i in range(1,6):    # using for loop
    print("*" * i)
    i = i + 1
"""

###########################################################