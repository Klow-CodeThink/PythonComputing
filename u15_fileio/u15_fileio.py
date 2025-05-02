# ###################################################
# # Part 1: Learning Exercises
    
# # Exercise 0: Getting Current Working Directory and File Path
# # Find the folder path for where your file is stored.
# # for github, need to append your repository name

# import os               # import os module
# filepath = os.getcwd()  # get current working directory
# print(filepath)

# # join the file path to get the full path
# fullpath = os.path.join(filepath,"file.txt")
# print(fullpath)

# # check existence of a file
# if os.path.exists(fullpath):
#     print("{} exist".format(fullpath))
# else:
#     print("{} does not exist".format(fullpath))

# #------------------------------------------------------------
# # Exercise 1: Open and Read Without 'with'
# # Open "example.txt", read its content, and close the file manually.
# # Ensure "example.txt" contains some text before running.

# file = open("example.txt", "r")  # Open in read mode
# content = file.read()           # Read entire content
# print("File content:\n{}".format(content))
# file.close()                    # Always close the file!

# #------------------------------------------------------------
# # Exercise 2: Write Without 'with'
# # Write "Manual Write Example" to "manual_output.txt" and close the file manually.

# file = open("manual_output.txt", "w")  # Open in write mode
# file.write("Manual Write Example")    # Write text to the file
# file.close()                          # Close the file to save changes

# #------------------------------------------------------------
# # Exercise 3: Read and Write Using 'with'
# # Read "example.txt" using 'with', ensuring the file closes automatically.

# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File content with 'with':\n{}".format(content))

# #------------------------------------------------------------
# # Write "Hello, World!" to "output.txt" using 'with'.

# with open("output.txt", "w") as file:
#     file.write("Hello, World!")

# #------------------------------------------------------------
# # Exercise 4: Append to File
# # Append "This is a new appended line." to "output.txt".

# with open("output.txt", "a") as file:
#     file.write("\nThis is a new appended line.")

# #------------------------------------------------------------
# # Exercise 5: Write Multiple Lines
# # Write a list of strings to "output.txt" using 'with'.

# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# with open("output.txt", "w") as file:
#     file.writelines(lines)

# #------------------------------------------------------------
# # Exercise 6: Read Line-by-Line
# # Open "example.txt" and read it line by line.

# with open("example.txt", "r") as file:
#     for line in file:
#         print("Line:", line.strip())  # Print each line

# ###################################################