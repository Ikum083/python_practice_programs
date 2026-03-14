# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
# ask user to input their name
full_name = str(input("Enter your full name: "))

# list to add every character
new_name_list = []


# function to turn every character to lower case using their ASCII values
def lower_case_name(full_name, new_name_list):
    for i in full_name:
        if 'A' <= i <= 'Z':
            new_name_list.append(chr(ord(i) + 32))
        else:
            new_name_list.append(i)

# print the letter
lower_case_name(full_name, new_name_list)
print(*new_name_list, sep='')