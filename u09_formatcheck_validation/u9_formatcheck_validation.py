###################################################
# Part 1: Learning Exercises

# Exercise 1: Converting to Uppercase
# Write a program to convert a string to uppercase.
# Example: Input = "hello", Output = "HELLO".

word = "hello"
uppercase_word = word.upper()                   # Convert to uppercase
print(f"Uppercase: {uppercase_word}")

#------------------------------------------------------------
# Exercise 2: Converting to Lowercase
# Write a program to convert a string to lowercase.
# Example: Input = "HELLO", Output = "hello".

word = "HELLO"
lowercase_word = word.lower()                   # Convert to lowercase
print(f"Lowercase: {lowercase_word}")

#------------------------------------------------------------
# Exercise 3: Checking if a String is Uppercase
# Write a program to check if a string is fully uppercase.
# Example: Input = "HELLO", Output = True.

word = "HELLO"
is_upper = word.isupper()                       # Check if uppercase
print(f"Is '{word}' uppercase? {is_upper}")

#------------------------------------------------------------
# Exercise 4: Checking if a String is Lowercase
# Write a program to check if a string is fully lowercase.
# Example: Input = "hello", Output = True.

word = "hello"
is_lower = word.islower()                       # Check if lowercase
print(f"Is '{word}' lowercase? {is_lower}")

#------------------------------------------------------------
# Exercise 5: Checking if a String is Alphanumeric
# Write a program to check if a string contains only letters 
# and numbers.
# Example: Input = "Python123", Output = True.

word = "Python123"
is_alnum = word.isalnum()                       # Check if alphanumeric
print(f"Is '{word}' alphanumeric? {is_alnum}")

#------------------------------------------------------------
# Exercise 6: Checking if a String is Alphabetic
# Write a program to check if a string contains only letters.
# Example: Input = "Python", Output = True.

word = "Python"
is_alpha = word.isalpha()                       # Check if alphabetic
print(f"Is '{word}' alphabetic? {is_alpha}")

#------------------------------------------------------------
# Exercise 7: Checking if a String is Numeric
# Write a program to check if a string contains only numbers.
# Example: Input = "12345", Output = True.

word = "12345"
is_digit = word.isdigit()                       # Check if numeric
print(f"Is '{word}' numeric? {is_digit}")

#------------------------------------------------------------
# Exercise 8: Removing Extra Spaces
# Write a program to remove leading and trailing spaces.
# Example: Input = "  hello  ", Output = "hello".

word = "  hello  "
stripped_word = word.strip()                    # Remove spaces
print(f"Stripped string: '{stripped_word}'")

#------------------------------------------------------------
# Exercise 9: Length Validation
# Write a program to validate that a string has at least 5 
# characters. Prompt the user repeatedly until they enter a 
# valid string.

while True:
    user_input = input("Enter a string with at least 5 characters: ")
    if len(user_input) >= 5:
        break                                   # Exit loop if valid
    print("String too short. Try again.")

print(f"Valid string: {user_input}")

###################################################