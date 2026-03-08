# list that contains all elements
numbers = []

# list that contains all elements after removing duplicates
final_numbers = []

# for loop to ask user to input 10 numbers
for i in range(10):
    user_input = float(input("Enter a number: "))
    numbers.append(user_input)

# another for loop to check if every element in the list has a duplicate
for j in numbers:
    if numbers.count(j) == 1:
        final_numbers.append(j)
    else:
        final_numbers.append(j)
        numbers.remove(j)

print(final_numbers)
# condition to remove the other iterations of said element