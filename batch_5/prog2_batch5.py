# ask user to input a number from 0 to 1000
user_input = int(input("Enter a number from 0 to 1000: "))

# condition to make sure input is within 0 to 1000
if user_input <= 1000 and user_input >= 0:  
    # f print to print the same digit except as a 6 digit number
    print(f"{user_input:06d}")
else:
    print("Wrong input!")