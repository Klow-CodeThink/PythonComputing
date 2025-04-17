
#####################################################

# Part 1: Learning Exercises
# Exercise 1: Simple Loop with range(stop)
# Write a program to print "Welcome to Python!" 5 times.
# Use range(stop) to repeat the message.
for _ in range(5):  # Loop runs 5 times
    print("Welcome to Python!")


#------------------------------------------------------------
# Exercise 2: Printing Numbers with range(stop)
# Write a program to print numbers from 0 to 4 using range(stop).
# Example: Output = 0, 1, 2, 3, 4.
for i in range(5):  # Loop from 0 to 4
    print("Number: {}".format(i))


#------------------------------------------------------------
# Exercise 3: Counting with range(start, stop)
# Write a program to print numbers from 10 to 15.
# Use range(start, stop) to set the range.
# Example: Output = 10, 11, 12, 13, 14, 15.
for i in range(10, 16):  # Loop from 10 to 15
    print("Counting: {}".format(i))


#------------------------------------------------------------
# Exercise 4: Using range(start, stop, step)
# Write a program to print even numbers from 2 to 10.
# Use range with a step value.
# Example: Output = 2, 4, 6, 8, 10.
for i in range(2, 11, 2):  # Step value is 2
    print("Even number: {}".format(i))


#------------------------------------------------------------
# Exercise 5: Printing Numbers in Reverse
# Write a program to print numbers from 10 to 1.
# Use range(start, stop, step) with a negative step value.
# Example: Output = 10, 9, 8, ..., 1.
for i in range(10, 0, -1):  # Loop backwards
    print("Countdown: {}".format(i))


#------------------------------------------------------------
# Exercise 6: Summing Numbers in a Range
# Write a program to calculate the sum of numbers from 1 to 10.
# Use range(start, stop) and a loop to add the numbers.
# Example: Output = 55.
total = 0
for i in range(1, 11):  # Loop from 1 to 10
    total += i
print("The total sum is: {}".format(total))


#------------------------------------------------------------
# Exercise 7: Printing a Simple Pattern
# Write a program to print the following pattern:
# *
# **
# ***
# ****
# *****
for i in range(1, 6):  # Loop for rows
    print("*" * i)


#####################################################