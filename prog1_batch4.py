# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
# list to contain all numbers
numbers = []

# for loop to ask user for 10 numbers
for i in range(10):
    user_input = float(input("Enter a number: "))
    numbers.append(user_input)

# condition to check for duplicates
for j in numbers:
    if numbers.count(j) != 1:
        # print duplicates
        print(j, end = ",")
