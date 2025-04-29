###########################################################
# Part 3: Challenge Exercises

# Exercise 1: Random Username Generator
# Write a function that generates a username based on the user's
# first name, last name, a random animal from a list, and a random number.

# List of random animals: ["Tiger", "Lion", "Bear", "Wolf", "Eagle"]
# Random number: Generated between 10 and 99

# Example:
# Input: First Name: "John", Last Name: "Doe"
# Random animal: "Tiger", Random number: 42
# Output: "JohnDoeTiger42"

"""
import random                                               # imports random module to pick animals and numbers randomly

def generate_username(first_name, last_name):               # defines a function that will generate the username when called
    animals = ["Tiger", "Lion", "Bear", "Wolf", "Eagle"]    # inside the function, a list of animals is defined

    ran_ani = random.choice(animals)                        # picks a random animal
    ran_num = random.randint(10,99)                         # picks a random number between 10 and 99
    
    username = f"{first_name}{last_name}{ran_ani}{ran_num}" # combines all 4 parts into one username string

    return username                                         # returns generated string to where it is called


first = input("Enter your first name: ")
last = input("Enter your last name: ")

user = generate_username(first, last)                       # returned username is called with the two names the user types
                                                            # it is stored in 'user'
print(f"Generated Username: {user}")                        # prints results
"""

#------------------------------------------------------------
# Exercise 2: Custom Greeting Generator
# Write a function that takes a list of names and randomly selects a greeting
# for each person from a predefined list of greetings, then prints a customized
# greeting for each person.

# List of greetings:
# ["Welcome to the event!", "Glad to have you here!", "It's great to see you!",
# "Thanks for joining us!"]

# Example:
# Input:
# Names: ["Alice", "Bob"]
 
 
# Output:
# "Hello Alice, Welcome to the event!"
# "Hello Bob, Thanks for joining us!"

"""
import random

def generate_msg(name):
    greetings = ["Welcome to the event!", "Glad to have you here!", "It's great to see you!", "Thanks for joining us!"]

    ran_greet = random.choice(greetings)

    message = f"Hello {name}, {ran_greet}"
    return message

person = input("Enter the person's name: ")

cust_msg = generate_msg(person)

print(cust_msg)
"""

#------------------------------------------------------------
# Exercise 3: Calculate Factorials
# Write a function that calculates the factorial of a number.

# Example:
# Input: Number: 5
# Output: "Factorial of 5 is 120"







#------------------------------------------------------------
# Exercise 4: Find Maximum in a List
# Write a function that takes a list of numbers and returns the maximum value.
# You must write the algorithm without using the max() function

# Example:
# Input: [12, 45, 7, 89, 23]
# Output: "The maximum value in the list is 89"

"""
def find_max(num_list):             # defines a function that takes a list of numbers
    max_num = num_list[0]           # starts by assuming the first number is the largest

    for num in num_list:            # loops through each number in the list
        if num > max_num:           # if a larger number is found, update max_num
            max_num = num

    return max_num                  # after the loop, returns the largest number found

numbers = [12, 45, 7, 89, 23]
max_value = find_max(numbers)
print(f"The maximum number is: {max_value}")
"""

#------------------------------------------------------------
# Exercise 5: Validate Email Address
# Write a function that validates an email address.

# Example:
# Input: "user@example.com"
# Output: "Valid email address."

# Input: "userexample.com"
# Output: "Invalid email address. Missing '@' or domain."







###########################################################
