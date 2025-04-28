###########################################################
# Part 2: IN-CLASS Practice Exercises

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
"""
# Task 1: Identify and print the name of the highest scoring student.


students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

high_score = 0
top_scorer = ""

for student, score in students.items():
    if score > high_score:
        high_score = score
        top_scorer = student

print(f"The highest scoring student is {top_scorer} with {high_score} marks.")


#------------------------------------------------------------
# Task 2: Calculate and display the number of students scoring above 80.


score_above80 = 0

for score in students.values():
    if score > 80:
        score_above80 = score_above80 + 1

print(f"The number of students scoring above 80 is {score_above80}.")


#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.


for stu in students:
    students[stu] = students[stu] + 5

print(students)
"""

#------------------------------------------------------------
# In-Class Exercise 2: Inventory Stock Management
# Scenario: A warehouse manager needs to manage product stock levels.

# Task 1: Add a new product "Pineapples" with an initial stock of 40.

inventory = {"Apples": 50, "Bananas": 30, "Oranges": 20, "Grapes": 60}

inventory["Pineapple"] = 40

print(inventory)


#------------------------------------------------------------
# Task 2: Find and print the total stock of all items combined.


tot_stock = 0

for stock in inventory.values():
    tot_stock = tot_stock + stock

print(f"The total stock of all items combined is {tot_stock}.")


#------------------------------------------------------------
# Task 3: Identify and remove any product with stock below 25.

to_remove = []                          # create a list to store items to remove*

for item, stock in inventory.items():
    if stock < 25:                      # find item with stock below 25
        to_remove.append(item)          # add to to_remove list*

for item in to_remove:                  # *
        del(inventory[item])            # remove items

print(f"Updated Inventory: {inventory}")


#------------------------------------------------------------
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Checked Out", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies.





#------------------------------------------------------------
# Task 2: Update the status of "1984" to "Checked Out" if all copies are borrowed.





#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.





#------------------------------------------------------------
# In-Class Exercise 4: Customer Orders Tracking
# Scenario: A store tracks orders with customers and the items they purchased.
orders = {
    "John": ["Apples", "Bananas"],
    "Mary": ["Oranges", "Grapes"],
    "Alice": ["Bananas", "Pineapples"],
}

# Task 1: Add a new order for "Mark" who purchased "Apples" and "Oranges".





#------------------------------------------------------------
# Task 2: Count and print the total number of unique items purchased by all customers.





#------------------------------------------------------------
# Task 3: Identify customers who purchased "Bananas".





###########################################################

