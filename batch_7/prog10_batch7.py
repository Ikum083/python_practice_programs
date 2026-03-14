# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
# string to be used
sample_word = "Hello World"

# char parameter to be used
iterated_char = 'l'

# function to mimick rindex()
def reversed_index(words_used, char_parameter) -> int:
## list that contains every character in the string
    characters = [x for x in words_used]
## reverse list content
    characters.reverse()
## use for loop to find first iteration of the char parameter
    for i in range(len(characters)):
        if characters[i] == char_parameter:
            ## return index
            return len(characters) - (i + 1)
        else:
            continue

# call function
iteration_index = reversed_index(sample_word, iterated_char)

# print result 
print(iteration_index)