###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").

"""
code = input("Enter the code: ")

uppercase_code = code.upper()
print(uppercase_code)
"""

#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols.

"""
username = input("Enter the username: ")

if username.isalnum():
    print("Username accepted.")
else:
    print("Invalid username. Only letters and numbers are allowed.")
"""

#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.

"""
phone_num = input("Enter the phone number: ")

if phone_num.isdigit():
    print("Valid number.")
else:
    print("Invalid number.")
"""

#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.

"""
feedback = input("Enter your feedback: ")

if "python" in feedback.lower():                # case insensitive
    print("Related to Python programming.")
else:
    print("Not related to Python programming.")
"""

#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").

"""
old_email = input("Enter your old email address: ")     # Get the user's old email address

old_domain = "@old.com"                                 # Define the old and new domains
new_domain = "@new.com"

if old_email.endswith(old_domain):                      # Check and replace the domain if it matches
    new_email = old_email.replace(old_domain, new_domain)
    print("Your updated email is:", new_email)
else:
    print("The email does not use the old domain. No changes made.")
"""

###########################################################