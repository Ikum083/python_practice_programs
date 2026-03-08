# boolean variable to control the while loop
asking_user = True

# while loop to keep asking user to input 
while asking_user:
# exception handle to stop while loop if value error is raised
    try:
        user_input = float(input("Enter a number: "))
    except ValueError:
        print("That's not a number!")
        asking_user = False