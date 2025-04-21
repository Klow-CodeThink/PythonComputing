# U4 - Exercise 1
# Write a program to print the following pyramid:
#     1
#    123
#   12345
#  1234567


#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 5
# 44
# 333
# 2222
# 11111
# counter algorithm 
count = 1

for i in range(5, 0, -1):  
    print(str(i) * count) 
    count = count + 1 ### same as change (count) by 1



# U4 - Exercise 2
# Write a program to generate the multiplication tables for
# any number.
# Example:
# Input = 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...

# num = int(input("Enter the number: "))

# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")


###########
# print out numbers from 0 - 16



# for i in range(0,17):
#     print(i)


# print out from 6 - 12

# for i in range(6,13):
#     print(i)

# print out from 3 - 13

# for i in range(3,14):
#     print(i)

# print out from 8 - 55

# for i in range(8,56):
#     print(i)

# print out from 10 - 13

# for i in range(10,14):
#     print(i)

# print out from 33 - 38

# for i in range(33,39):
#     print(i)

# print out from 88 - 90

# for i in range(88,91):
#     print(i)

# print out from 1025 - 1030

# for i in range(1025,1031):
#     print(i)

# print out from 88 - 90
 
# for i in range(88,91):
#     print(i)




# range (start, stop, step)

# print out multiples of 6 from 6 to 72

# for i in range(6,73,6):
#     print(i)


# print out even numbers from 2 to 8

# for i in range(2,9,2):
#     print(i)

# print out odd numbers from 5 to 13

# for i in range(5,14,2):
#     print(i)

# count down 1 by 1 from 13 - 5

# for i in range(13,-6,-1):
#     print(i)


# num1 = input("What is the first number? ") ## always gives a string value
# num2 = input("What is the second number? ")

# int() str()


###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Printing Odd Numbers
# Write a program to print all odd numbers from 1 to 15.
# Use range(start, stop, step) to skip even numbers.
# Example: Output = 1, 3, 5, ..., 15.



#------------------------------------------------------------
# Exercise 9: Multiplying Numbers
# Write a program to print the first 5 multiples of 7.
# Use range(start, stop, step).
# Example: Output = 7, 14, 21, 28, 35.


#------------------------------------------------------------
# Exercise 10: Repeating a Phrase
# Write a program to print "I love Python!" 3 times.
# Use range(stop) to repeat the phrase.



#------------------------------------------------------------
# Exercise 11: Custom Counting Pattern
# Write a program to print the following pattern:
# 5
# 44
# 333
# 2222
# 11111




#------------------------------------------------------------
# Exercise 12: Generating a Multiplication Table
# Write a program to print the multiplication table of 6.
# Example: 6 x 1 = 6, ..., 6 x 10 = 60.




#------------------------------------------------------------
# Exercise 13: Printing a Custom Star Pattern
# Write a program to print the following pattern:
# *
# ***
# *****
# *******
# *********


####
# math test - 10 questions
# the computer will generate 2 random numbers
# ask for addition of these 2 numbers
# every time correct, you will +1 to score
# at end of 10 questions show the score