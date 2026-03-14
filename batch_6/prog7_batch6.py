# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
# string to be centered
example_word = "Hello"

# character to fill in space 
fill_character = "*"

# function to mimick center()
def center_string(word_to_be_used, length_desired, char_to_fill):
    # list to contain every character in the sample word
    character_list = []
    
    # append every character to the character list
    for i in word_to_be_used:
        character_list.append(i)

    # while loop to check if the length of the character is equal to the desired length
    while len(character_list) <= length_desired:
        # condition where the difference of the desired length and the length of the character list is even
        if (length_desired - len(character_list)) % 2 == 0:
            character_list.append(char_to_fill)
            character_list.insert(0, char_to_fill)
        # condition where the difference of the desired length and the length of the character list is odd
        else:
            right_additions = ((length_desired - len(character_list)) // 2) + 1
            left_additons =  ((length_desired - len(character_list)) // 2)
            for i in range(right_additions):
                character_list.append(char_to_fill)
            for j in range(left_additons):
                character_list.insert(0, char_to_fill)
    # print the new character
    else:
        # print new string
        print(*character_list, sep = "")

# call function
center_string(example_word, 10, fill_character)