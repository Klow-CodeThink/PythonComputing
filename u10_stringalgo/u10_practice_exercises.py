###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Case-Insensitive Substring Search
# Scenario: Searching for "python" in a string, ignoring case.

"""
text = "I love PYTHON programming."

if "python" in text.lower():
    print("The word 'python' is found.")
else:
    print("The word 'python' is not found.")
"""

#------------------------------------------------------------
# Exercise 9: Multiple Occurrences of Substring
# Scenario: Find all positions where "Python" appears in a string.
# text = "Python is great. Python is easy to learn. Python is fun!"

"""
text = "Python is great. Python is easy to learn. Python is fun!"

word = "Python"                 # Word to search

positions = []                  # List to store positions

index = 0                       # Starting index for search


while index < len(text):        # Loop to find all occurrences
    index = text.find(word, index)
    if index == -1:
        break
    positions.append(index)
    index += len(word)          # Move past the current match to avoid infinite loop


print(f"Positions where 'Python' appears: {positions}")
"""

#------------------------------------------------------------
# Exercise 10: Manual List Splitting
# Scenario: A list of comma-separated numbers is given, and you 
# need to split it into individual elements without using .split().
data = "10,20,30,40,50"






#------------------------------------------------------------
# Exercise 11: Finding All Positions Without .find()
# Scenario: Find all positions where a word appears in a sentence 
# manually without using .find() or .index().
text = "Python is Python, and Python is fun."





###########################################################