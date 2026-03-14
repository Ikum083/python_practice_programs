# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
# ask user to input name with many spaces at the beginning
full_name = str(input("Enter your name with many spaces before it: "))

# function to remove the spaces in the input
new_name = " ".join(full_name.split())

# print cleaned name
print(new_name)