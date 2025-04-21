
# Common Example for validation
# infinite loop
"""
while True:
    answer = int(input("What is 1 + 1? "))

# check if answer is correct

    if answer == 2:
        print("Correct.")
        break
    else:
        print("Wrong.")
"""

"""
while True:
    answer = input("What is a deer with no eyes? ")
    if answer.lower() == "no idea":
        print("Correct.")
        break
    else:
        print("Wrong.")
"""

"""
# Ex7
i = 1
num = 5

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i = i + 1
"""

"""
# Ex8
count = 1 # 1, 2, 3, ...
sum = 0

while count <= 5:
    # sum all the numbers
    sum = sum + count
    count = count + 1

print(f"The sume is {sum}")
"""

"""
#Ex9
import random

rannum = random.randint(1,10)
print(rannum)

while True:
    guess = int(input("What is my number? "))

    if guess == rannum:
        print("Your guess is correct.")
        break
    else:
        print("Wrong.")
"""

"""
# Ex10

password = "passwd"

while True:
    password = input("What is the password? ")

    if password == password:
        print("Access granted.")
        break
    else:
        print("Access denied.")
"""

# Ex11

