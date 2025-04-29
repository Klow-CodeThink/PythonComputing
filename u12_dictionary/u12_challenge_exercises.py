###########################################################
# Part 3: Challenge Exercises

# Challenge: Advanced Grade Analysis
# Scenario: A teacher needs detailed analysis of class performance.
"""
# Task 1: Find and print the names of students who scored below the average grade.

students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}


tot_score = 0

for score in students.values():
    tot_score = tot_score + score

# print(tot_score)

avg_grade = tot_score / len(students)

print(f"The average grade is {avg_grade} marks.")

avg_grade_stu = []

for student, score in students.items():
    if score < avg_grade:
        avg_grade_stu.append(student)

print(f"Students who scored below the average grade: {avg_grade_stu}")


# Task 2: Create a new dictionary with students categorized as "Pass" or "Fail".
# Assume a passing grade is 80 or above. 


Pass_Fail = {}

for student, score in students.items():
    if score >= 80:
        Pass_Fail[student] = "Pass"
    else:
        Pass_Fail[student] = "Fail"


print(Pass_Fail)

# or

stu_pass = {}
stu_fail = {}

for student, score in students.items():
    if score >= 80:
        stu_pass[student] = score
    else:
        stu_fail[student] = score

print(f"Students who passed: {stu_pass}")
print(f"Students who failed: {stu_fail}")
"""

#------------------------------------------------------------
# Exercise 2: Inventory Reordering System
# Scenario: A warehouse manager needs to identify items for reordering.
inventory = {"Apples": 50, "Bananas": 10, "Oranges": 20, "Grapes": 5, "Pineapples": 40}

# Task 1: Identify and print items with stock below 15 for reordering.







# Task 2: Calculate and print the percentage of total stock for each item.







#------------------------------------------------------------
# Exercise 3: Library System Enhancements
# Scenario: A librarian wants to track book borrow history.
books = {
    "1984": {"status": "Available", "copies": 5, "borrowed": 3},
    "Brave New World": {"status": "Checked Out", "copies": 0, "borrowed": 5},
    "Fahrenheit 451": {"status": "Available", "copies": 2, "borrowed": 1},
}

# Task 1: Identify the book with the highest borrow count.







# Task 2: Add a new book and simulate borrowing it twice.







#------------------------------------------------------------
# Exercise 4: Complex Order Tracking
# Scenario: A store manager tracks customers, their orders, and the total bill.
orders = {
    "John": {"items": {"Apples": 3, "Bananas": 2}, "total": 15},
    "Mary": {"items": {"Oranges": 1, "Grapes": 4}, "total": 20},
    "Alice": {"items": {"Bananas": 5, "Pineapples": 2}, "total": 25},
}

# Task 1: Add a new order for Mark with 2 Apples and 3 Oranges. Assume $3 per Apple and $4 per Orange.







# Task 2: Identify the customer with the highest total bill.







###########################################################