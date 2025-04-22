###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Scenario: A user accidentally adds duplicate items to their
# shopping list. Write a program to remove duplicate items.
# Your program is a shopping list program.
# 1. Program will keep asking user to input a shopping list again and again until user indicates otherwise.
# 2. Code a user menu to add, view, or delete items from a menu
# 3. Code the delete function, you need to validate that the item is in the menu before deletion.
# Example:
# Input = ["apple", "banana", "apple", "orange"],
# Output = ["apple", "banana", "orange"].

"""
fruits = ["apple", "banana", "apple", "orange"]
del(fruits[2])
print(fruits)
"""

#------------------------------------------------------------
# Exercise 2
# Scenario: 
# You have a list of words from a document and want to remove a specific word
# (e.g., "singapore") to clean it up.
# Example:
# passage_1 = ["the", "singapore", "river", "once", "the", "lifeline", "of", "singapore", "trade", "and", "commerce", "was", "notoriously", "polluted", "in", "the", "past", "singapore", "faced", "significant", "challenges", "as", "waste", "from", "industries", "and", "homes", "flowed", "into", "the", "singapore", "river", "however", "singapore", "initiated", "an", "ambitious", "cleanup", "transforming", "the", "singapore", "river", "into", "a", "symbol", "of", "singapore", "commitment", "to", "urban", "sustainability", "and", "progress"]
# Remove "singapore".

"""
passage_1 = ["the", "singapore", "river", "once", "the", "lifeline", "of", "singapore", "trade", "and", "commerce", "was", "notoriously", "polluted", "in", "the", "past", "singapore", "faced", "significant", "challenges", "as", "waste", "from", "industries", "and", "homes", "flowed", "into", "the", "singapore", "river", "however", "singapore", "initiated", "an", "ambitious", "cleanup", "transforming", "the", "singapore", "river", "into", "a", "symbol", "of", "singapore", "commitment", "to", "urban", "sustainability", "and", "progress"]

for p in passage_1:
    if p == "singapore":
        passage_1.remove("singapore")

print(passage_1)
"""

#------------------------------------------------------------
# Exercise 3
# Scenario: A contest ranks participants based on scores.
# Write a program to find the second highest score from a list.
# Example: 
# Input = [87, 95, 76, 88, 95]
# Output = 88.





###########################################################