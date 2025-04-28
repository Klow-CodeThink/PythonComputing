###########################################################
# Part 2: IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
numbers = [10, 20, 30, 40, 50, 60, 70]


midindex = len(numbers) // 2 # floor divide 2 # gives the centre index

print(numbers[midindex - 1 : midindex + 2])




#------------------------------------------------------------
# Exercise 8: Checking Palindrome in a String
# Scenario: Determine if a string is a palindrome (reads the same 
# backward as forward).
word = input("Enter a word: ").lower()

if word == word[::-1]:
    print("The word is a palindrom.")
else:
    print("The word is not a palindrom.")


#------------------------------------------------------------
# Exercise 9: Reversing Words in a Sentence
# Scenario: Reverse the words in a sentence manually.
sentence = "Python is fun to learn."







#------------------------------------------------------------
# Exercise 10: Validating a Substring
# Scenario: Check if a string contains only alphabets using slicing.
text = "Hello123"







###########################################################