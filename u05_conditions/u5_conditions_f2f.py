##################################################
# Part 1: Learning Exercises [F2F]

# Comparison Operators
# ==       >> equal to
# !=       >> not equal to    
# >        >> more than
# <        >> less than
# >=       >> more than or equal to
# <=       >> less than or equal to

#------------------------------------------------------------
# Check if the number is equal to, more than or less than

num1 = 10 #input("Enter first number: ")
num2 = 10 #input("Enter second number: ")
if num1 == num2:
    print(f"{num1} is equals to {num2}")

elif num1 > num2:
    print(f"{num1} is more than {num2}")

else:
    print(f"{num1} is less than {num2}")

#------------------------------------------------------------
# Explanation on if-elif-else
# multiple permutations based on a single input

hour = int(input("What hour is it? ")) # 24h clock

if hour < 7:
    print("Get ready for school. ")
elif hour < 8:
    print("Assembly. ")
elif hour < 9:
    print("Math")
elif hour < 10:
    print("Recess")
elif hour < 11:
    print("Science")
elif hour < 12:
    print("Chinese")
else:
    print("Go home.")

#------------------------------------------------------------
# Get computer to think of a random number between 1 - 100

import random # random library
rannum = random.randint(1,100)
print(rannum)

# repeat this process 7 times

for i in range (7):

    # computer will ask me to guess

    guess = int(input("Guess my number (1-100): "))


    # check if number is more than

    if guess > rannum:
        print(f"{guess} is too big. Try again.")

    # check if number is less than

    elif guess < rannum:
        print(f"{guess} is too small. Try again.")

    # check if number is equals to

    else:
        print(f"{guess} is correct!")
        break

else:  # if guess != rannum:
    print("You did not guess it.")
    print(f"The number is {rannum}.")

##################################################
