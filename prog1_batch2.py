numbers = []

for i in range(2):
    user_number = float(input("Enter a number: "))
    numbers.append(user_number)

numbers.sort()

print(numbers[0])