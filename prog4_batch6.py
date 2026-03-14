# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
# input to ask user for their full name
full_name = str(input("Enter your full name: "))

# list to put every character in the new name
new_name_list = []

# function to upper case every character
def to_uppper_case(full_name, new_name_list):
    for i in full_name:
        if 'a' <= i <= 'z':
            new_name_list.append(chr(ord(i) - 32))
        else:
            new_name_list.append(i)

# print new name
to_uppper_case(full_name, new_name_list)
print(*new_name_list, sep = '')