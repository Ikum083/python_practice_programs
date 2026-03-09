# list to contain all user input
numbers = []

# variable to control while loop
asking_user = True

# while loop with exception handling to ask for user input and terminate while loop when invalid input
while asking_user:
    try:
        user_input = float(input("Enter a number: "))
        numbers.append(user_input)
    except ValueError:
        print("Invalid input!")
        asking_user = False

# sort list from highest to lowest

# print every element from list