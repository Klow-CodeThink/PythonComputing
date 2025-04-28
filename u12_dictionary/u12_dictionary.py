###################################################
# Part 1: Learning Exercises

# Practice Exercise 1: Creating a Dictionary
# Create a dictionary to store student names and their grades.

students = {"Alice": 85, "Bob": 90, "Charlie": 78} # answer

#------------------------------------------------------------
# Practice Exercise 2: Accessing Dictionary Values
# Access Bob's grade from the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}

bobgrade = students["Bob"] # pull out a value using the key
print(bobgrade)

#------------------------------------------------------------
# Practice Exercise 3: Adding New Key-Value Pairs
# Add a new student, Diana, with a grade of 92 to the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}

students["Diane"] = 92 # add a new key / value to the end of the dictionary
print(students)

#------------------------------------------------------------
# Practice Exercise 4: Updating Existing Values
# Update Charlie's grade to 80 in the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}

students["Charlie"] = 80
print(students)

# if the key does not exist, then it will add
# if the key already exists, it will update

#------------------------------------------------------------
# Practice Exercise 5: Deleting Key-Value Pairs
# Remove Alice's entry from the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}

del(students["Alice"])
print(students)

#------------------------------------------------------------
# Practice Exercise 6: Checking for Existence of a Key
# Check if 'Diana' is in the student dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}

stu = "Diana"

if stu in students:
    print(f"{stu} is in the class.")
else:
    print(f"{stu} is not in the class.")

#------------------------------------------------------------
# Practice Exercise 7: Iterating Through a Dictionary
# Print all student names and their grades.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}


# to read the values only

for stu, score in students.items():     #.items() pulls out both key and value

    print(f"{stu} scored {score}.")

    
# or

# to be able to amend the value

for stu in students: # stu is the key

    # print(stu)            # key
    
    # print(students[stu])  # value from the dictionary using the key

    # print(f"{stu} scored {students[stu]}.")

    students[stu] = students[stu] - 10

print(students)

###################################################
