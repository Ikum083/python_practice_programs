first_num = float(input("Enter a number: "))

for i in range(9):
    next_num = float(input("Enter another number: "))
    next_num = first_num - next_num
    print(next_num)

