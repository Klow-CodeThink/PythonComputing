###########################################################
# Part 3: Challenge Exercises

# Exercise 1: Extracting Initials from a Name
# Scenario: A company wants to display initials for employees on ID cards.
# Given a full name, extract the initials.

# Example:
# Input: "John Michael Smith"
# Output: "J.M.S"

# Input: "Alice Bob"
# Output: "A.B"

"""
full_name = input("Enter your full name: ").strip() # .strip removes extra space at start and end

name_parts = full_name.split()                      # .split separates the name wherever there's a space (turning it into a list).

ini_ext = ""                                        # create an empty variable to put the initials

for part in name_parts:                             # loop through each part and take the first letter
    ini_ext = ini_ext + part[0] + "."

print(f"The initials for {full_name} is {ini_ext}.")
"""

#------------------------------------------------------------
# Exercise 2: Finding Common Elements in Two Lists
# Scenario: A school maintains two lists—
# one for students enrolled in a club and another for students who paid membership fees.
 
# Identify students who are both enrolled and have paid.

# Example:
# Input:
# club_members = ["Alice", "Bob", "Charlie", "David"]
# paid_members = ["Charlie", "David", "Eve"]
# Output: ["Charlie", "David"]

# Input:
# club_members = ["John", "Paul", "George", "Ringo"]
# paid_members = ["Paul", "George"]
# Output: ["Paul", "George"]

"""
club_members = ["John", "Paul", "George", "Ringo"]
paid_members = ["Paul", "George"]

enroll_paid = []                        # create an empty list for enrolled and paid

for student in club_members:            # loops through every student in club_members
    if student in paid_members:         # checks if that student also in paid_members
        enroll_paid.append(student)     # if yes, add that student to new list enroll_paid 

print(enroll_paid)
"""

#------------------------------------------------------------
# Exercise 3: Reversing Letters of Each Word
# Scenario: A text-based encryption system reverses the letters of 
# each word in a sentence to obscure its meaning.
 
# Write a program to simulate this.

# Example:
# Input: "Python is fun"
# Output: "nohtyP si nuf"

# Input: "Hello world"
# Output: "olleH dlrow"

"""
sentence = input("Enter a sentence to encrypt: ")       # Ask user for input sentence

words = sentence.split()                                # Split the sentence into words

revword_list = []                                       # Create a list to store reversed words

for word in words:
    revword = word[::-1]                                # Slice to reverse each word
    revword_list.append(revword)                        # Add reversed word to list


encryp_sentence = " ".join(revword_list)                # Join reversed words back into a sentence

print(encryp_sentence)
"""

#------------------------------------------------------------
# Exercise 4: Extracting Even-Indexed Elements
# Scenario:
# A temperature monitoring device records hourly temperatures over a day.
# Extract data for even hours (0, 2, 4, etc.) for analysis.

# Example:
# Input: hourly_temperatures = [22, 23, 21, 24, 20, 25, 19, 26]
# Output: [22, 21, 20, 19]

# Input: hourly_temperatures = [30, 31, 32, 33, 34, 35]
# Output: [30, 32, 34]

"""
hourly_temperatures = [22, 23, 21, 24, 20, 25, 19, 26]

print(hourly_temperatures[::2])
"""

###########################################################