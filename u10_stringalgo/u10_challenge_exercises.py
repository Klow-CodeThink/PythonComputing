###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Scenario: You are comparing two sentences to find common words between them.

# Example:
 
# Input:
# sentence1 = "Python is fun and powerful."
# sentence2 = "Python is powerful and versatile."
# Output: ["Python", "is", "powerful", "and"]

# Input:
# sentence1 = "I love programming in Python."
# sentence2 = "Python programming is versatile."
# Output: ["Python", "programming"]

# Input:
# sentence1 = "This is a test."
# sentence2 = "Completely different sentence."
# Output: []

"""
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

common_words = words1 & words2      # common_words = words1.intersection(words2)

print(f"The common words are {common_words}.")
"""

#------------------------------------------------------------
# Exercise 2
# Scenario: Count how many times each word appears in a paragraph.

# Example:
 
# Input:
# paragraph = "Python is great. Python is easy. Python is fun."
 
# Output:
# ["Python", "is", "great", "easy", "fun"]
# [3,3,1,1,1]







#------------------------------------------------------------
# Exercise 3
# Scenario: Reverse the words in a sentence without using built-in methods.

# Example:
# Input: "Python is fun to learn."
# Output: "learn to fun is Python"

# Input: "The quick brown fox jumps."
# Output: "jumps fox brown quick The"

# Input: "Hello world."
# Output: "world Hello"

sentence = "Python is fun to learn"

# split into a list
slist = sentence.split(" ")
print(slist)

revsen = "" # empty string

for word in slist:
    revsen = word + " " + revsen

print(revsen)

###########################################################