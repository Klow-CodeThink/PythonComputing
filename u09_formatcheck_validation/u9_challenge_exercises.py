###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# - At least one uppercase letter.
# - At least one lowercase letter.
# - At least one digit.

# Example:
# Input: "Secure123"
# Output: "Valid password"

# Input: "password"
# Output: "Invalid password"

"""
password = input("Enter the password: ")

has_upper = False
has_lower = False
has_digit = False

for pw in password:
    if pw.isupper():
        has_upper = True
    elif pw.islower():
        has_lower = True
    elif pw.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Valid password")
else:
    print("Invalid password")
"""

#------------------------------------------------------------
# Exercise 2
# Scenario: Ensure a sentence starts with a capital letter and ends with a period.

# Example:
# Input: "The quick brown fox jumps over the lazy dog."
# Output: "Valid sentence"

# Input: "the quick brown fox jumps over the lazy dog"
# Output: "Invalid sentence: does not start with a capital letter 
#           Invalid sentence: does not end with a period"

# Input: "Hello world"
# Output: "Invalid sentence: does not end with a period"


sentence = input("Enter a sentence: ")

has_cap = False
has_stop = False

for c in sentence:
    if c.isupper():
        has_cap = True
    elif c.endswith("."):
        has_stop = True

if not has_cap:
    print("Invalid sentence: does not start with a capital letter")

if not has_stop:
    print("Invalid sentence: does not end with a full stop")

if has_cap and has_stop:
    print("Valid sentence")

# else:
#     print("Invalid sentence")


#------------------------------------------------------------
# Exercise 3
# Scenario: Count the number of uppercase letters in a paragraph.

# Example:
# Input: "The Quick Brown Fox Jumps Over The Lazy Dog."
# Output: "Number of uppercase letters: 8"

# Input: "this is a simple paragraph with no uppercase letters."
# Output: "Number of uppercase letters: 0"

# Input: "Hello, World! Python Is Amazing."
# Output: "Number of uppercase letters: 4"

"""
count = 0

para = input("Enter a paragraph: ")

for letter in para:
    if letter.isupper():
        count = count + 1

print(f"Number of uppercase letters: {count}")
"""

###########################################################