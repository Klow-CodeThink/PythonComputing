###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 8: Pass/Fail Checker
# Write a program to check if a student's score is a pass or 
# fail. Passing marks are 50 and above. Example: Input = 65.
# Output: "Pass."

"""
number = 65
if number >= 50:
    print("Pass.")
"""

#------------------------------------------------------------

# Exercise 9: Finding the Largest of Three Numbers
# Write a program to find the largest of three numbers.
# Example: Input = 4, 7, 2. Output = "The largest is 7."

"""
num1 = 4
num2 = 7
num3 = 2
if num1 > num2 and num1 > num3:
    print(f"The largest number is {num1}.")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")
"""

#------------------------------------------------------------
# Exercise 10: Leap Year Checker
# Write a program to check if a year is a leap year.
# Example: Input = 2024. Output = "Leap year."






#------------------------------------------------------------
# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20+).
# Example: Input = 15. Output = "Teen."

"""
age = int(input("Enter Age: "))
if age >= 1 and age <= 12:
    print("Child.")
elif age >= 13 and age <= 19:
    print("Teen.")
else:
    print("Adult.")
"""

#------------------------------------------------------------
# Exercise 12: Grade Checker
# Write a program to assign a grade based on marks:
# >= 90: A, >= 75: B, >= 60: C, < 60: D.
# Example: Input = 85. Output = "Grade B."

"""
marks = int(input("Enter the marks: "))
if marks >= 90:
    print(f"Grade A.")
elif marks >= 75:
    print(f"Grade B.")
elif marks < 60:
    print(f"Grade C.")
"""

#------------------------------------------------------------
# Exercise 13: Even/Odd Checker
# Write a program to check if a number is even or odd.
# Example: Input = 4. Output = "Even number."

"""
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")
"""

###########################################################