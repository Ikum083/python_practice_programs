# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# ask user to input their full name with improper casing
full_name = str(input("Enter your full name with improper casing: "))

# print full name using .replace() and .title() to print in pascal case
print(f"{(full_name.title()).replace(' ', '')}")
