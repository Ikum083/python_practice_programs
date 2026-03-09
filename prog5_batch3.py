# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
# variables to be used : sum of all user input, number of all inputs and bool to control the while loop
input_sum = 0
input_quantity = 0
asking_input = True

# while loop to keep asking user to input numbers until failure
while asking_input:
    # exception handling
    try:
        input_sum += float(input("Enter a number: "))
        input_quantity += 1
    except ValueError:
        print("Wrong input!")
        asking_input = False

# divide the sum of all inputs and number of inputs

# print result