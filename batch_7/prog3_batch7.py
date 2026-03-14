# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
# string to be used
sample_word = "Hello World"

# function to change ASCII number of every char in the string
def all_caps(word_used):
    # list to contain every character in the sample word
    characters = [x for x in sample_word]
    # for loop to check for every character in the sample word
    for i in range(len(characters)):
    ## conditions to capitalize every lower case character
        if 'a' <= characters[i] <= 'z':
            characters[i] = chr(ord(characters[i]) - 32)
        else:
            continue
    # print new word
    print(*characters, sep = '') 

all_caps(sample_word)


