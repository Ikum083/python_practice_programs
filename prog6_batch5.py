# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
# have user input their full name with improper casing
full_name = str(input("Enter your full name in improper casing: "))

# print each character in reverse casing
print(full_name.swapcase())