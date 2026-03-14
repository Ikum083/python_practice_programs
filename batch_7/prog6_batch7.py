# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
# sample string
sample_word = "Hello"

# desired length
desired_length = 10

# character to be used for fill
char_fill = "_"

# function to mimick rjust()
def begin_adjust(word_used, length, fill):
    ## list that contains every character in the list
    characters = [x for x in sample_word]
    ## while loop to keep inserting character fill until it meets the desired length
    while len(characters) != desired_length:
        characters.insert(0, fill)
    else:
        ## print result
        print(*characters, sep = '')

# call function
begin_adjust(sample_word, desired_length, char_fill)