###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.

"""
numbers = [10, 20, 30, 40, 50, 60, 70]

mid_index = len(numbers) // 2   # floor divide 2 --> gives the centre index

print(numbers[mid_index - 1 : mid_index + 2])   # mid_index - 1 --> index left of centre index
                                                # mid_index + 2 --> index right of centre index
"""

#------------------------------------------------------------
# Exercise 8: Checking Palindrome in a String
# Scenario: Determine if a string is a palindrome (reads the same 
# backward as forward).

"""
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("The word is a palindrom.")
else:
    print("The word is not a palindrom.")
"""

#------------------------------------------------------------
# Exercise 9: Reversing Words in a Sentence
# Scenario: Reverse the words in a sentence manually.

"""
sentence = "Python is fun to learn"

split_list = sentence.split(" ")    # split into a list
print(split_list)

rev_sen = ""                        # empty string to put the words in reverse

for word in split_list:
    rev_sen = word + " " + rev_sen

print(rev_sen)
"""

#------------------------------------------------------------
# Exercise 10: Validating a Substring
# Scenario: Check if a string contains only alphabets using slicing.

"""
text = "Hello"

only_letters = True     # assume contain all letters

for i in range(len(text)):
    if not text[i].isalpha():
        only_letters = False
        break

if only_letters:
    print("The text contains only alphabets.")
else:
    print("The text does not contain only alphabets.")
"""

###########################################################


