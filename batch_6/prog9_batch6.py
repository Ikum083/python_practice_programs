# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
# string to be used
sample_word = "hello world"

# function to mimick capitalize
def capital_string(word_used):
    # list to be used in the function
    character_list = [x for x in word_used]
    if 'a' <= character_list[0] <= 'z':
        character_list[0] = chr(ord(character_list[0]) - 32)
    print(*character_list, sep = "") 

# call function
capital_string(sample_word)