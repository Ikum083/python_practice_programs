# list to store all numbers
numbers = []

# ask user to input 10 numbers
for i in range(10):
    user_input = float(input("Enter a number: "))
    numbers.append(user_input)

# count how many of a number appears in the list
for j in numbers:
    element_amount = numbers.count(j)
    if element_amount == 1:
# print out numbers with no duplicates
        print(f"Element with no duplicate: {j}")
    else:
        continue