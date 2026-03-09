# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
# bool variable to control for loop and variable to store largest number
asking_user = True
largest_num = 0

# while loop to keep asking user for input
while asking_user:
    user_input = float(input("Enter a number: "))
    if user_input >= largest_num:
        largest_num = user_input
    else:
        continue

# print largest number