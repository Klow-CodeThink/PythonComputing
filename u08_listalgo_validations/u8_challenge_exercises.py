###########################################################
# Part 3: Challenge Exercises

# Exercise 1
# Scenario: Comparing inventories to find shared products between two stores.
# Given 2 lists, find the common items between the 2 lists.
# Add the common items into another list called common and print them out.

"""
list_a = ["apple", "banana", "cherry", "date", "elderberry"]
list_b = ["banana", "cherry", "date", "fig", "grape"]

common = []                         # Find common items

for item in list_a:
    if item in list_b:
        common.append(item)

print(f"Common items: {common}")    # Print the common items
"""

#------------------------------------------------------------
# Exercise 2
# Scenario: Ranking scores to determine the runner-up.
# Find the second and third place winners in this list.
 
scores = [90, 85, 92, 88, 76, 95, 89, 70]




#------------------------------------------------------------
# Exercise 3
# Scenario: Managing a queue where the first person moves to the back.

"""
queue = ["Person1", "Person2", "Person3", "Person4", "Person5"]

# after code runs
# queue = ["Person2", "Person3", "Person4", "Person5", "Person1"]


# Remove the first person and add them to the end
first_person = queue.pop(0)     # Removes "Person1"
queue.append(first_person)      # Adds "Person1" to the back


print(f"Updated queue: {queue}")  # Print the updated queue
"""

###########################################################
