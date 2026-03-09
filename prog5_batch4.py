# variables to be used : bool to control the while loop, sum of all inputs and number of inputs
asking_user = True
sum_user_input = 0
input_quantity = 0

# while loops with exception handling to ensure user inputs only integers
while asking_user:
    try:
        sum_user_input += float(input("Enter a number: "))
        input_quantity += 1
    except ValueError:
        print("Invalid input!")
        asking_user = False
# compute for average

# print average