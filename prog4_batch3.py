## Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
# list to contain all numbers
numbers = []

# variable to control the while loop
asking_input = True
# while loop to keep asking user for inputs until it raises an error
while asking_input:
    try:
        user_input = float(input("Enter a number: "))
    except ValueError:
        print("Input is invalid!")
        asking_input = False
# conditon to check if the user's input is the lowest number

# print lowest number