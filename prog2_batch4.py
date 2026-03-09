# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
# list to contain all numbers
numbers = []

# bool variable to control while loop
asking_input = True

# while loop with exception handling to ask for user input
while asking_input:
    user_input = float(input("Enter a number: "))
    numbers.append(user_input)

# for loop to check the count of every element in the list

# dictionary to store element with their respective count

# print element with the most duplicates based on dicitonary