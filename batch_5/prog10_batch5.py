# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
# ask user to input their full name
full_name = str(input("Enter your full name with improper casing: "))

# print full name in snake case using .lower() and .replace()
print(f"{(full_name.lower()).replace(" ", "_")}")