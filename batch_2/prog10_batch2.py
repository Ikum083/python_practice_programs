numbers = []

for i in range(2):
    user_num = int(input("Enter a number: "))
    numbers.append(user_num)

numbers.sort()

temp_number = numbers[1]
for i in range(numbers[1] - numbers[0] - 1):
    temp_number -= 1
    print(temp_number, end = ",")