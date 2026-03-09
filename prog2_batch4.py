# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
# list to contain all numbers
numbers = []

# bool variable to control while loop
asking_input = True

# while loop with exception handling to ask for user input
while asking_input:
    try:
        user_input = float(input("Enter a number: "))
        numbers.append(user_input)
    except ValueError:
        print("Invalid input!")
        asking_input = False

# dictionary to store element with their respective count
element_quantities = {}

# for loop to check the count of every element in the list
for i in numbers:
    # store number with their respective quantity in the dicionary
    element_quantities[f"{i}"] = numbers.count(i)
    # remove every iterarion of said element to avoid duplication
    numbers = [x for x in numbers if x != i]

# find the number with the largest amount of duplicates 
most_duplicated_num = max(element_quantities, key = element_quantities.get)

# print element with the most duplicates based on dicitonary
print(most_duplicated_num)