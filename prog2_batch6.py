# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
# ask user to input their full name 
full_name = str(input("Enter your full name: "))

# split name into seperate elements in a list
seperated_name = full_name.split()

# function to remove the first name
del seperated_name[0]

# print the new name
for i in seperated_name:
    print(i, end = " ")