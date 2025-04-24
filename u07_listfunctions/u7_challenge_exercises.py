###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Scenario:  Your program is a shopping list program.
# 1. Program will keep asking user to input a shopping list 
    # again and again until user indicates otherwise (e.g. stop)
# 2. Enhance your program to check if the item already exists in list
    # if already exists, display a message to say it already exists
    # if not exist, then add the item to the list


shoplist = []                                       # initialise shopping list at the start

print("Welcome to K Store.")

# start the main loop

while True:
    item = input("\nWhat do you want to buy? ")     # ask user

    if item.lower() == "stop":                      # end program
        print("\nDone with shopping list.")
        break
    else:
        if item not in shoplist:
            shoplist.append(item)
        else:
            print(f"\n{item} is already in the shopping list.")

# print out shopping list
print("\nThese items are in your shopping list: ")

for i in range(len(shoplist)):                      # (alternative) for i in shoplist:
    print(f"{i+1}. {shoplist[i]}")                  # (alternative) print(i)

 
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