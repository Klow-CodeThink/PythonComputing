###################################################
# Part 1: Learning Exercises

# Practice Exercise 1: Creating a Dictionary
# Create a dictionary to store student names and their grades.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Student Grades: {}".format(students))

#------------------------------------------------------------
# Practice Exercise 2: Accessing Dictionary Values
# Access Bob's grade from the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
bob_grade = students["Bob"]  # Access using the key
print("Bob's grade is: {}".format(bob_grade))

#------------------------------------------------------------
# Practice Exercise 3: Adding New Key-Value Pairs
# Add a new student, Diana, with a grade of 92 to the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["Diana"] = 92  # Add new key-value pair
print("Updated Student Grades: {}".format(students))

#------------------------------------------------------------
# Practice Exercise 4: Updating Existing Values
# Update Charlie's grade to 80 in the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["Charlie"] = 80  # Update value
print("Updated Student Grades: {}".format(students))

#------------------------------------------------------------
# Practice Exercise 5: Deleting Key-Value Pairs
# Remove Alice's entry from the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
del students["Alice"]  # Delete key-value pair
print("Updated Student Grades: {}".format(students))

#------------------------------------------------------------
# Practice Exercise 6: Checking for Existence of a Key
# Check if 'Diana' is in the student dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
if "Diana" in students:
    print("Diana is in the dictionary.")
else:
    print("Diana is not in the dictionary.")

#------------------------------------------------------------
# Practice Exercise 7: Iterating Through a Dictionary
# Print all student names and their grades.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
for name, grade in students.items():  # Iterate through dictionary
    print("{}: {}".format(name, grade))

###################################################