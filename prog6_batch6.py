# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
# string variable to be used
full_name = "Hello"

# character to be used to add in the list
character_to_be_used = "_"

# function to add characters in the list given
def left_adjust(string_to_be_used, word_length, seperating_char):
    # list to contain every character in the string
    name_characters = []
    for i in string_to_be_used:
        name_characters.append(i)

    while len(name_characters) != word_length:
        name_characters.append(seperating_char)
    else:
        # print new word
        print(*name_characters, sep = "")

left_adjust(full_name, word_length = 10, seperating_char= character_to_be_used)