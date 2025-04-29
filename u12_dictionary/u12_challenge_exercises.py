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
"""
# Task 1: Identify and print items with stock below 15 for reordering.

inventory = {"Apples": 50, "Bananas": 10, "Oranges": 20, "Grapes": 5, "Pineapples": 40}


for_reorder = []

for item, stock in inventory.items():
    if stock < 15:
        for_reorder.append(item)

print(f"Items with stock below 15 for reordering: {for_reorder}")


# Task 2: Calculate and print the percentage of total stock for each item.

total_stock = sum(inventory.values())

for item, stock in inventory.items():
    percent_item = (stock / total_stock) * 100
    print(f"{item} : {percent_item:.0f}%")
"""

#------------------------------------------------------------
# Exercise 3: Library System Enhancements
# Scenario: A librarian wants to track book borrow history.
"""
# Task 1: Identify the book with the highest borrow count.

books = {
    "1984": {"status": "Available", "copies": 5, "borrowed": 3},
    "Brave New World": {"status": "Checked Out", "copies": 0, "borrowed": 5},
    "Fahrenheit 451": {"status": "Available", "copies": 2, "borrowed": 1},
}


high_borrow_count = 0
top_book = ""

for book, details in books.items():
    if details["borrowed"] > high_borrow_count:
        high_borrow_count = details["borrowed"]
        top_book = book

print(f"The book with the highest count of {high_borrow_count} borrows is '{top_book}'.")


# Task 2: Add a new book and simulate borrowing it twice.

# add a new book + details
books["To Kill a Mockingbird"] = {"status": "Available", "copies": 6, "borrowed": 0}


while True:
    choice = input(f"Which book would you like to borrow: ")
    
    if choice.lower() == "end":
        break

    if choice in books:
        if books[choice]["copies"] > 0:
            books[choice]["copies"] -= 1
            books[choice]["borrowed"] +=1
            print(f"Book successfully borrowed. Go to the counter to collect.")
            
            if books[choice]["copies"] == 0:
                books[choice]["status"] = "Checked Out"
                print(f"{choice} is now Checked Out.")
        
        else:
            print(f"{choice} is not available. All copies have been checked out.")
    
    else:
        print(f"{choice} is not available in this library.")

print("\nUpdated Inventory")
for book, details in books.items():
    print(f"{book}: {details}")
"""

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