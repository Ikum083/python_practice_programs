# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# ask user to input a statement
user_statement = str(input("Enter a full statement: "))

# printf number of characters in said input
print(f"{len(user_statement.split())}")